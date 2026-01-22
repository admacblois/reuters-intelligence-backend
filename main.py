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
        print(f"Searching for: {payload.query}")
        
        # 1. Gerar Embedding da pergunta
        query_vector = get_embedding(payload.query)
        
        # 2. Buscar no Supabase
        response = supabase.rpc("match_documents", {
            "query_embedding": query_vector,
            "match_threshold": 0.1, 
            "match_count": 5
        }).execute()
        
        matches = response.data
        
        # Se não achou nada (Fallback em Inglês)
        if not matches:
            return {
                "status": "success",
                "data": {
                    "summary": "I could not find information about this in the current technical manuals (WNE, FTP, Liaison). Please try rephrasing your question.",
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
                "title": meta.get("title", "Untitled"),
                "url": meta.get("url", "#"),
                "type": "doc"
            })
            # Adiciona o trecho ao contexto que o GPT vai ler
            context_text += f"Document: {meta.get('title')}\nContent: {match.get('content')}\n---\n"

        # 4. A MÁGICA: Gerar a resposta com GPT-4o (Agora 100% em Inglês)
        print("🧠 Generating AI response...")
        
        # --- AQUI ESTÁ A MUDANÇA CRÍTICA ---
        system_prompt = """
        You are the Reuters Platform Engineering Assistant.
        Your role is to answer technical questions based STRICTLY on the provided context.
        
        CRITICAL GUIDELINES:
        1. LANGUAGE: You must ALWAYS answer in ENGLISH. Even if the user asks in Portuguese, Spanish, or any other language, your output must be in professional technical English.
        2. Be direct, technical, and professional.
        3. If the context mentions steps or configurations (IPs, ports, hardware), list them in bullet points.
        4. Cite which manual contains the information (e.g., "According to the DL360 Installation Manual...").
        5. If the answer is not in the context, state that you do not have that information. DO NOT invent information.
        """

        user_prompt = f"""
        User Question: {payload.query}

        Context Retrieved from Manuals:
        {context_text}
        """

        completion = openai_client.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2 
        )

        final_answer = completion.choices[0].message.content

        return {
            "status": "success",
            "data": {
                "summary": final_answer, 
                "confidence_score": matches[0].get("similarity", 0.0),
                "sources": sources_list,
                "related_queries": ["Hardware Specifications", "Network Configuration"] 
            }
        }

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
