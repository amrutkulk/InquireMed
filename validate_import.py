# validate_imports.py

def test_imports():
    modules = [
        "streamlit", "pandas", "numpy", "requests", "tqdm",
        "transformers", "datasets", "sentence_transformers",
        "nltk", "spacy", "biopython", "lxml",
        "chromadb", "faiss", "langchain", "llama_index"
    ]
    
    for mod in modules:
        try:
            __import__(mod)
            print(f"✅ {mod} imported successfully")
        except ImportError:
            print(f"❌ {mod} failed to import")

if __name__ == "__main__":
    test_imports()
