import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from supabase import create_client, Client
from openai import OpenAI

# Inicializa o App
app = FastAPI(title="Reuters Intelligence API")

# --- Configuração de Clientes (Supabase & OpenAI) ---
# O Railway injeta essas variáveis automaticamente (já configuramos lá)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validação simples para não crashar se faltar chave
if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERRO CRÍTICO: Variáveis do Supabase não encontradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# --- Configuração de CORS (Permite o Lovable acessar) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, troque pela URL do Lovable
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modelos de Dados (Contrato com o Frontend) ---
class UserContext(BaseModel):
    role: Optional[str] = "user"
    region: Optional[str] = "global"

class QueryRequest(BaseModel):
    query: str
    user_context: Optional[UserContext] = None

class SourceItem(BaseModel):
    id: str
    title: str
    url: str
    type: str

class IntelligenceResponse(BaseModel):
    status: str
    data: dict

# --- Funções Auxiliares ---
def get_embedding(text: str):
    """Gera o vetor da pergunta para buscar no banco"""
    response = openai_client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

# --- Endpoints ---

@app.get("/")
def read_root():
    return {"system": "Reuters Intelligence Backend", "status": "online", "mode": "semantic-search"}

@app.post("/api/v1/search", response_model=IntelligenceResponse)
async def search_intelligence(payload: QueryRequest):
    try:
        print(f"Buscando por: {payload.query}")
        
        # 1. Gerar Embedding da pergunta
        query_vector = get_embedding(payload.query)
        
        # 2. Buscar no Supabase (RPC Call)
        # Chama a função 'match_documents' que criamos no SQL
        response = supabase.rpc("match_documents", {
            "query_embedding": query_vector,
            "match_threshold": 0.5, # Ajuste a sensibilidade aqui
            "match_count": 5
        }).execute()
        
        matches = response.data
        
        # 3. Montar a resposta
        sources_list = []
        context_text = ""
        
        for match in matches:
            # Extrai metadados
            meta = match.get("metadata", {})
            sources_list.append({
                "id": str(match.get("id")),
                "title": meta.get("title", "Sem título"),
                "url": meta.get("url", "#"),
                "type": "doc"
            })
            context_text += f"{match.get('content')}\n---\n"

        # Se não achou nada relevante
        if not matches:
            return {
                "status": "success",
                "data": {
                    "summary": "Desculpe, não encontrei informações relevantes na base de conhecimento da Reuters Intelligence sobre esse tópico.",
                    "confidence_score": 0.0,
                    "sources": [],
                    "related_queries": []
                }
            }

        # 4. (Opcional) Gerar Resumo com GPT-4o usando o contexto encontrado
        # Por enquanto, retornamos uma resposta estática baseada no contexto para economizar,
        # mas aqui entraria a chamada de ChatCompletion para gerar o texto final.
        summary_text = f"Encontrei {len(matches)} documentos relevantes.\n\n### Contexto Encontrado:\n{context_text[:500]}..." 
        
        return {
            "status": "success",
            "data": {
                "summary": summary_text, # Futuramente: Resposta do GPT
                "confidence_score": matches[0].get("similarity", 0.9),
                "sources": sources_list,
                "related_queries": ["Como configurar SSO", "Erro de acesso"] # Placeholder
            }
        }

    except Exception as e:
        print(f"Erro no processamento: {e}")
        raise HTTPException(status_code=500, detail=str(e))