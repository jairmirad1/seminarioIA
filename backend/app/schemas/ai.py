from pydantic import BaseModel, Field
from typing import Literal

class ChatMessage(BaseModel):
    """A single message in the chat history."""
    role: Literal["user", "assistant"] = Field(description="The role of the message sender.")
    content: str = Field(description="The text content of the message.")

class ChatRequest(BaseModel):
    """Request for the conversational SQL generation process."""
    messages: list[ChatMessage] = Field(description="The full conversation history including the new prompt.")

class SQLGenerationRequest(BaseModel):
    """Request for the SQL generation process (Legacy)."""
    prompt: str = Field(description="The natural language prompt in Spanish to translate into SQL.")

class SQLGenerationResult(BaseModel):
    """Result of the SQL generation process."""
    sql: str = Field(description="The generated PostgreSQL-compatible SQL SELECT query.")
    explanation: str = Field(description="A brief explanation in Spanish of what the query does.")
    results: list[dict] | None = Field(default=None, description="The results of executing the SQL query.")
