import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
N_RESULTS = 5
CHROMA_COLLECTION = "utd_cs_prof_guide"
CHROMA_PATH = "./chroma_db"
DOCS_PATH = "./documents"
