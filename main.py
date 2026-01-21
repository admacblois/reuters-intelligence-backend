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
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERRO CRÍTICO: Variáveis do Supabase não encontradas.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# --- Configuração de CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modelos de Dados ---
class UserContext(BaseModel):
    role: Optional[str] = "user"
    region: Optional[str] = "global"

class QueryRequest(BaseModel):
    query: str
    user_context: Optional[UserContext] = None

class IntelligenceResponse(BaseModel):
    status: str
    data: dict

# --- Funções Auxiliares ---
def get_embedding(text: str):
    response = openai_client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

# --- Endpoints ---
@app.get("/")
def read_root():
    return {"system": "Reuters Intelligence Backend", "status": "online", "mode": "generative-ai"}

@app.post("/api/v1/search", response_model=IntelligenceResponse)
async def search_intelligence(payload: QueryRequest):
    try:
        print(f"Buscando por: {payload.query}")
        
        # 1. Gerar Embedding da pergunta
        query_vector = get_embedding(payload.query)
        
        # 2. Buscar no Supabase
        response = supabase.rpc("match_documents", {
            "query_embedding": query_vector,
            "match_threshold": 0.1, # Mantivemos baixo para garantir resultados
            "match_count": 5
        }).execute()
        
        matches = response.data
        
        # Se não achou nada
        if not matches:
            return {
                "status": "success",
                "data": {
                    "summary": "Não encontrei informações sobre isso nos manuais técnicos atuais (WNE, FTP, Liaison). Tente reformular a pergunta.",
                    "confidence_score": 0.0,
                    "sources": [],
                    "related_queries": []
                }
            }

        # 3. Montar o Contexto para o GPT
        sources_list = []
        context_text = ""
        
        for match in matches:
            meta = match.get("metadata", {})
            sources_list.append({
                "id": str(match.get("id")),
                "title": meta.get("title", "Sem título"),
                "url": meta.get("url", "#"),
                "type": "doc"
            })
            # Adiciona o trecho ao contexto que o GPT vai ler
            context_text += f"Documento: {meta.get('title')}\nConteúdo: {match.get('content')}\n---\n"

        # 4. A MÁGICA: Gerar a resposta com GPT-4o
        print("🧠 Gerando resposta com IA...")
        
        system_prompt = """
        Você é o Assistente de Engenharia de Plataformas da Reuters.
        Sua função é responder dúvidas técnicas baseando-se ESTRITAMENTE no contexto fornecido.
        
        Diretrizes:
        1. Seja direto, técnico e profissional.
        2. Se a informação estiver no contexto, explique-a claramente.
        3. Se o contexto mencionar passos ou configurações (IPs, portas, hardware), liste-os em tópicos.
        4. Cite qual manual contém a informação (ex: "Segundo o manual de Instalação do DL360...").
        5. Se a resposta não estiver no contexto, diga que não sabe. NÃO invente.
        """

        user_prompt = f"""
        Pergunta do Usuário: {payload.query}

        Contexto Recuperado dos Manuais:
        {context_text}
        """

        completion = openai_client.chat.completions.create(
            model="gpt-4o", # O modelo mais inteligente
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2 # Baixa temperatura = Mais precisão, menos alucinação
        )

        final_answer = completion.choices[0].message.content

        return {
            "status": "success",
            "data": {
                "summary": final_answer, # A resposta inteligente vem aqui!
                "confidence_score": matches[0].get("similarity", 0.0),
                "sources": sources_list,
                "related_queries": ["Especificações de Hardware", "Configuração de Rede"] 
            }
        }

    except Exception as e:
        print(f"Erro no processamento: {e}")
        raise HTTPException(status_code=500, detail=str(e))
