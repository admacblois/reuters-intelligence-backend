import os
import pandas as pd
import re
from langchain_community.document_loaders import DataFrameLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# --- CONFIGURATION ---
CSV_PATH = "knowledge_export.csv"
DOCS_FOLDER = "documents"
PERSIST_DIRECTORY = "./chroma_db"

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("⚠️ Please set your OPENAI_API_KEY environment variable.")

def clean_text(text):
    if not isinstance(text, str): return ""
    text = re.sub(r'<[^>]+>', ' ', text) # Strip HTML
    return re.sub(r'\s+', ' ', text).strip()

def ingest_hybrid():
    print("--- INITIATING MEGA-CHUNK INDEXING PROTOCOL ---")
    documents = []

    # 1. INTERNAL KNOWLEDGE (CSV)
    if os.path.exists(CSV_PATH):
        print(f"🔹 Indexing Knowledge Base: {CSV_PATH}")
        df = pd.read_csv(CSV_PATH)
        df['combined_text'] = (
            "SOURCE_TYPE: Salesforce Knowledge Article\n" + 
            "TITLE: " + df['Title'].fillna('') + "\n" + 
            "CONTENT: " + df['Answer__c'].apply(clean_text)
        )
        loader = DataFrameLoader(df, page_content_column="combined_text")
        documents.extend(loader.load())

    # 2. DOCUMENT VAULT
    if os.path.exists(DOCS_FOLDER):
        print(f"🔹 Scanning Vault: {DOCS_FOLDER}")
        for file in os.listdir(DOCS_FOLDER):
            file_path = os.path.join(DOCS_FOLDER, file)
            
            # A. Smart Markdown (From LlamaParse)
            if file.endswith(".md"):
                print(f"   ✓ Indexing Smart Doc: {file}")
                loader = TextLoader(file_path)
                docs = loader.load()
                for d in docs: d.metadata['source'] = file
                documents.extend(docs)
            
            # B. PDF (Fallback)
            elif file.endswith(".pdf"):
                # Check if we have a smart version first
                if os.path.exists(file_path.replace(".pdf", ".md")):
                    continue
                print(f"   ✓ Indexing Standard PDF: {file}")
                loader = PyPDFLoader(file_path)
                docs = loader.load()
                for d in docs: d.metadata['source'] = file
                documents.extend(docs)

    # 3. VECTORIZATION (THE FIX IS HERE)
    if not documents:
        print("❌ ERROR: No documents found.")
        return

    print(f"🔹 Vectorizing {len(documents)} document sources...")
    
    # CRITICAL CHANGE: Increased chunk_size from 1000 to 8000.
    # This ensures long lists/tables are NOT cut in half.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=8000, 
        chunk_overlap=500,
        separators=["\n\n", "\n", " ", ""] # Try to split by paragraphs first
    )
    
    split_docs = text_splitter.split_documents(documents)
    
    if os.path.exists(PERSIST_DIRECTORY):
        import shutil
        shutil.rmtree(PERSIST_DIRECTORY)
        
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Batch processing to avoid hitting limits with large chunks
    batch_size = 100
    for i in range(0, len(split_docs), batch_size):
        batch = split_docs[i:i+batch_size]
        Chroma.from_documents(batch, embeddings, persist_directory=PERSIST_DIRECTORY)
        print(f"   - Processed batch {i}/{len(split_docs)}")
        
    print(f"✅ SUCCESS: Mega-Chunk Knowledge Graph created with {len(split_docs)} nodes.")

if __name__ == "__main__":
    ingest_hybrid()
