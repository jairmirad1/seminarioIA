from pydantic import BaseModel, Field

class SQLGenerationResult(BaseModel):
    """Result of the SQL generation process."""
    sql: str = Field(description="The generated PostgreSQL-compatible SQL SELECT query.")
    explanation: str = Field(description="A brief explanation in Spanish of what the query does.")
