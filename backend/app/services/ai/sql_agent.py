import os
from pathlib import Path
from pydantic_ai import Agent, RunContext
from app.core.config import settings
from app.schemas.ai import SQLGenerationResult

# Define the path to the schema DDL
SCHEMA_PATH = Path(__file__).parent.parent.parent / "models" / "football_schema.sql"

# Ensure the agent library can discover the key from settings.
if settings.google_api_key and not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = settings.google_api_key

def load_schema() -> str:
    """Load the football database schema DDL."""
    if not SCHEMA_PATH.exists():
        return "-- Schema not found"
    return SCHEMA_PATH.read_text(encoding="utf-8")

SYSTEM_INSTRUCTIONS = (
    "Eres un experto en SQL y análisis de datos de fútbol de élite. "
    "Tu tarea es traducir preguntas en lenguaje natural (español) a consultas SQL válidas y optimizadas "
    "compatibles con SQLite para una base de datos de los 50 mejores jugadores del mundo.\n\n"
    "REGLAS CRÍTICAS:\n"
    "1. SOLO puedes generar sentencias 'SELECT'.\n"
    "2. NUNCA generes sentencias DML o DDL (INSERT, UPDATE, DELETE, DROP, etc.).\n"
    "3. Utiliza ÚNICAMENTE las tablas y columnas definidas en el esquema proporcionado a continuación.\n"
    "4. Si la pregunta no se puede responder con el esquema proporcionado, explica por qué.\n"
    "5. La explicación debe ser breve, profesional y en español.\n"
    "6. El esquema utiliza una estructura relacional con tablas: 'equipos', 'jugadores', 'partidos' y 'estadisticas'.\n"
    "7. REGLA CRÍTICA PARA GENERACIÓN DE SQL: Siempre que una consulta involucre tablas con claves foráneas (como equipo_id, equipo_local_id, equipo_visitante_id o jugador_id), DEBES USAR SIEMPRE operaciones JOIN para devolver los nombres reales legibles (ej. equipos.nombre o jugadores.nombre_completo) en lugar de los IDs numéricos brutos. Nunca devuelvas un SELECT con números de claves foráneas a menos que se soliciten explícitamente.\n\n"
    f"ESQUEMA DE LA BASE DE DATOS:\n{load_schema()}"
)

# Initialize the Pydantic AI Agent
# Note: Ensure GOOGLE_API_KEY is set in the environment or in backend/.env
sql_agent = Agent(
    'google:gemini-2.5-flash',
    output_type=SQLGenerationResult,
    system_prompt=SYSTEM_INSTRUCTIONS
)
