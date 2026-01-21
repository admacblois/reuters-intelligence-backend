import os
import nest_asyncio
from llama_parse import LlamaParse

# --- CONFIGURATION ---
LLAMA_CLOUD_API_KEY = "llx-L1Qor0TXlbvPQIpCot46Xi5osic1HWRogmcB24ez1QYVZH1M"
DOCS_FOLDER = "documents"

# Apply nest_asyncio to allow running in scripts/notebooks
nest_asyncio.apply()

def convert_pdfs_to_markdown():
    print("--- STARTING INTELLIGENT CONVERSION ---")
    
    if not os.path.exists(DOCS_FOLDER):
        print(f"Error: Folder '{DOCS_FOLDER}' not found.")
        return

    # Initialize the Parser (set to Markdown for best AI readability)
    parser = LlamaParse(
        api_key=LLAMA_CLOUD_API_KEY,
        result_type="markdown",  # Markdown is actually better than JSON for LLMs to read
        verbose=True
    )

    files = [f for f in os.listdir(DOCS_FOLDER) if f.endswith(".pdf")]
    
    if not files:
        print("No PDFs found to convert.")
        return

    for pdf_file in files:
        full_path = os.path.join(DOCS_FOLDER, pdf_file)
        print(f"Processing: {pdf_file}...")
        
        try:
            # 1. Parse the PDF
            documents = parser.load_data(full_path)
            
            # 2. Save as Markdown (Text file)
            # We change extension from .pdf to .md
            output_filename = pdf_file.replace(".pdf", ".md")
            output_path = os.path.join(DOCS_FOLDER, output_filename)
            
            with open(output_path, "w", encoding="utf-8") as f:
                # Join all pages into one text
                full_text = "\n\n".join([doc.text for doc in documents])
                f.write(full_text)
                
            print(f"✅ Success! Saved intelligent extraction to: {output_filename}")
            
        except Exception as e:
            print(f"❌ Failed to convert {pdf_file}: {e}")

    print("--- CONVERSION COMPLETE ---")
    print("You can now run 'ingest.py'. It will pick up these new smart .md files.")

if __name__ == "__main__":
    convert_pdfs_to_markdown()
