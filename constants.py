import os
import chromadb


from chromadb.config import Settings

# Define the new Chroma settings
CHROMA_SETTINGS = {
    "chroma_db_impl": "duckdb+parquet",
    "persist_directory": "db",
    "anonymized_telemetry": False
}

# Create a Settings object with the new settings
settings = Settings(**CHROMA_SETTINGS)