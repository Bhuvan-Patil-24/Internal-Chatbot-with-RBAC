import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base project directory (root of project)
BASE_DIR = Path(__file__).resolve().parent.parent  # adjust if config is nested deeper

class Config:
    # JWT Settings
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 5
    REFRESH_TOKEN_EXPIRE_DAYS = 7

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Vector DB / Data paths
    DATA_DIR = BASE_DIR / "data"
    LOGS_DIR = BASE_DIR / "logs"

    VECTOR_DB_PATH = DATA_DIR / "vector_db"
    EMBEDDINGS_PATH = DATA_DIR / "chunk_embeddings.npy"
    CHUNKS_PATH = DATA_DIR / "all_chunks.json"
    METADATA_PATH = DATA_DIR / "all_metadata.json"
    ABBREVIATIONS_PATH = DATA_DIR / "ABBREVIATIONS.json"
    RBAC_PERMISSIONS_PATH = DATA_DIR / "rbac_permissions.json"

    # Embedding Model
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # LLM Settings
    OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
    HF_API_TOKEN = os.getenv("HF_API_TOKEN")
    LLM_PROVIDER = "hf_mistral"  # "ollama", "huggingface", "hf_mistral"
    LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.2" # Options: "mistral", "google/flan-t5-base", "mistralai/Mistral-7B-Instruct-v0.2"

    # RAG Settings
    TOP_K_RETRIEVAL = 4
    SIMILARITY_THRESHOLD = 0.3
    MAX_CONTEXT_LENGTH = 2000

    # Audit Logging
    AUTH_LOG_FILE = LOGS_DIR / "auth_audit.log"
    ACCESS_LOG_FILE = LOGS_DIR / "access_audit.log"
    RAG_LOG_FILE = LOGS_DIR / "rag_audit.log"
