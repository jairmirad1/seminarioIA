import os
from pathlib import Path
from pydantic_ai import Agent, RunContext
from app.schemas.ai import SQLGenerationResult

# Define the path to the schema DDL
SCHEMA_PATH = Path(__file__).parent.parent.parent / "models" / "football_schema.sql"

def load_schema() -> str:
    """Load the football database schema DDL."""
    if not SCHEMA_PATH.exists():
        return "-- Schema not found"
    return SCHEMA_PATH.read_text(encoding="utf-8")

# Initialize the Pydantic AI Agent
# Note: Ensure GOOGLE_API_KEY is set in the environment
sql_agent = Agent(
    'google:gemini-1.5-flash',
    result_type=SQLGenerationResult,
    system_prompt=(
        "Eres un experto en SQL y análisis de datos de fútbol. "
        "Tu tarea es traducir preguntas en lenguaje natural (español) a consultas SQL válidas y optimizadas "
        "compatibles con PostgreSQL.\n\n"
        "REGLAS CRÍTICAS:\n"
        "1. SOLO puedes generar sentencias 'SELECT'.\n"
        "2. NUNCA generes sentencias DML o DDL (INSERT, UPDATE, DELETE, DROP, etc.).\n"
        "3. Utiliza ÚNICAMENTE las tablas y columnas definidas en el esquema proporcionado a continuación.\n"
        "4. Si la pregunta no se puede responder con el esquema proporcionado, explica por qué.\n"
        "5. La explicación debe ser breve y en español.\n\n"
        f"ESQUEMA DE LA BASE DE DATOS:\n{load_schema()}"
    )
)
