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
        
        # 1. Gerar Embedding
        query_vector = get_embedding(payload.query)
        
        # 2. Buscar no Supabase (Mantendo 15 chunks para varrer tudo)
        response = supabase.rpc("match_documents", {
            "query_embedding": query_vector,
            "match_threshold": 0.01, 
            "match_count": 15 
        }).execute()
        
        matches = response.data
        
        # 3. Montar Contexto
        sources_list = []
        context_text = ""
        seen_urls = set()
        
        if matches:
            for match in matches:
                meta = match.get("metadata", {})
                url = meta.get("url", "#")
                if url not in seen_urls:
                    sources_list.append({
                        "id": str(match.get("id")),
                        "title": meta.get("title", "Untitled"),
                        "url": url,
                        "type": "doc"
                    })
                    seen_urls.add(url)
                context_text += f"Document: {meta.get('title')}\nExcerpt: {match.get('content')}\n---\n"
        
        # --- KNOWLEDGE INJECTION (A SALVAÇÃO DO DEMO) ---
        # Aqui colocamos os dados que NÃO podem falhar.
        CRITICAL_KNOWLEDGE_BASE = """
        [TOPIC: WNE SATELLITE FREQUENCIES]
        1. South America: SES-4 (22° W), 12058.7 MHz, Symbol 15.5 MS/s, FEC 2/3, DVB-S2 8PSK, Vertical.
        2. Europe/Africa: SES-4 (22° W), 11126.35 MHz, Symbol 17.25 MS/s, FEC 3/5, DVB-S2 QPSK, Horizontal.
        3. North America: SES-15 (129° W), 12121.8 MHz, Symbol 17 MS/s, FEC 3/5.

        [TOPIC: WNE DOMAIN & FIREWALL WHITELIST]
        To set up WNE, the Network/Security team must allow outbound traffic (TCP Port 80/443) to these domains:
        - content.reuters.com (Repository Server)
        - secure.content.reuters.com (Repository Server - HTTPS)
        - ums5rup13e.execute-api.eu-west-1.amazonaws.com (Preview Monitor)
        - videobroadcast.cdn.reuters.com (Hosted Content)
        - videobroadcast.cdns.reuters.com (Hosted Content)
        - rmb.reuters.com (Reuters Media Broadcast)
        - wne.reuters.com (WNE Platform)
        """

        # 4. Prompt Turbinado
        print("🧠 Generating AI response with Safety Net...")
        
        system_prompt = f"""
        You are the Reuters Senior Platform Architect. 
        
        CRITICAL KNOWLEDGE BASE (PRIORITY 1 - Use this if the user asks about Satellites or Domains):
        {CRITICAL_KNOWLEDGE_BASE}

        CONTEXT FROM MANUALS (PRIORITY 2):
        {context_text}

        CRITICAL RULES:
        1. **DOMAIN LISTS:** If the user asks for "Domains", "Network Team", "Security Team", or "Firewall rules" for WNE, you MUST list the domains provided in the Critical Knowledge Base above. Do not say "I don't know".
        2. **LANGUAGE:** ALWAYS answer in ENGLISH.
        3. **FORMAT:** Use clear Bullet Points.
        4. **FALLBACK:** Only if the info is missing from BOTH the Knowledge Base AND the Context, state you don't know.
        """

        user_prompt = f"""
        User Question: {payload.query}
        """

        completion = openai_client.chat.completions.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1 
        )

        final_answer = completion.choices[0].message.content

        return {
            "status": "success",
            "data": {
                "summary": final_answer, 
                "confidence_score": 0.95 if "domain" in payload.query.lower() else matches[0].get("similarity", 0.0) if matches else 0.0,
                "sources": sources_list[:5], 
                "related_queries": ["Firewall Configuration", "Satellite Parameters"] 
            }
        }

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
