import os
from typing import List
from pypdf import PdfReader
from supabase import create_client, Client
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis (se existirem)
load_dotenv()

# --- ÁREA DAS CHAVES (COLE AQUI DENTRO DAS ASPAS) ---
SUPABASE_URL = "key"
SUPABASE_KEY = "key"
OPENAI_API_KEY = "key"

# --- Conexão Direta (Sem try/except para não dar erro) ---
print("🔌 Conectando aos serviços...")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text: str):
    # Remove quebras de linha para melhorar o vetor
    text = text.replace("\n", " ")
    return openai_client.embeddings.create(input=[text], model="text-embedding-3-small").data[0].embedding

def process_pdf(file_path: str):
    print(f"📖 Lendo: {file_path}...")
    try:
        reader = PdfReader(file_path)
    except Exception as e:
        print(f"   ⚠️ Erro ao abrir PDF {file_path}: {e}")
        return []

    file_name = os.path.basename(file_path)
    chunks = []
    
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            
            if text:
                # Remove caractere Nulo (\x00) que quebra o Postgres
                text = text.replace("\x00", "") 
                
                if len(text) > 100: # Ignora páginas quase vazias
                    chunks.append({
                        "content": text,
                        "metadata": {
                            "title": file_name,
                            "url": f"local://{file_name}",
                            "page": i + 1
                        }
                    })
        except Exception as e:
            print(f"   ⚠️ Pulei a página {i+1} por erro de leitura: {e}")
            continue
            
    print(f"   -> Extraídos {len(chunks)} trechos relevantes.")
    return chunks

def ingest_folder(folder_path="docs"):
    if not os.path.exists(folder_path):
        print(f"Pasta '{folder_path}' não encontrada.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    
    if not files:
        print("Nenhum PDF encontrado na pasta docs.")
        return

    print(f"Iniciando ingestão de {len(files)} arquivos...")

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        chunks = process_pdf(file_path)
        
        for chunk in chunks:
            try:
                vector = get_embedding(chunk["content"])
                
                data = {
                    "content": chunk["content"],
                    "metadata": chunk["metadata"],
                    "embedding": vector
                }
                
                supabase.table("documents").insert(data).execute()
                print(f"      ✅ Salvo: Pág {chunk['metadata']['page']}")
            except Exception as e:
                print(f"      ❌ Erro ao salvar Pág {chunk['metadata']['page']}: {e}")

    print("\n🚀 Ingestão concluída com sucesso!")

if __name__ == "__main__":
    ingest_folder()
