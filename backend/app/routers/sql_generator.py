import logging
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    UserPromptPart,
    TextPart,
    SystemPromptPart,
)
from app.schemas.ai import ChatRequest, SQLGenerationResult
from app.services.ai.sql_agent import sql_agent, SYSTEM_INSTRUCTIONS
from app.core.database import get_db

logger = logging.getLogger("api.routers.sql_generator")

router = APIRouter(tags=["sql-generator"])

def map_history_to_messages(history: List) -> List[ModelMessage]:
    """
    Map simple {role, content} history to Pydantic AI ModelMessage structures.
    """
    messages: List[ModelMessage] = []
    
    # Inject system instructions as the first message
    messages.append(ModelRequest(parts=[SystemPromptPart(content=SYSTEM_INSTRUCTIONS)]))
    
    for msg in history:
        if msg.role == "user":
            messages.append(ModelRequest(parts=[UserPromptPart(content=msg.content)]))
        elif msg.role == "assistant":
            # Assistant messages in our app are typically the explanation or SQL
            # For simplicity, we store the content as a TextPart
            messages.append(ModelResponse(parts=[TextPart(content=msg.content)]))
            
    return messages

@router.post("/generate-sql", response_model=SQLGenerationResult)
async def generate_sql(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Generate a SQL SELECT query from conversational context and execute it.
    """
    if not request.messages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Messages list cannot be empty"
        )
        
    # The last message is the current prompt
    current_message = request.messages[-1]
    if current_message.role != "user":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The last message must be from the user"
        )
        
    prompt = current_message.content
    # Everything before the last message is history
    history_raw = request.messages[:-1]
    message_history = map_history_to_messages(history_raw)
    
    logger.info("POST /generate-sql prompt=%s, history_len=%d", prompt, len(history_raw))
    
    try:
        # Run the agent with message history
        agent_result = await sql_agent.run(prompt, message_history=message_history)
        output = agent_result.output
        
        # Execute the generated SQL if present
        if output.sql:
            try:
                sql_result = db.execute(text(output.sql))
                # Convert results to list of dicts
                results = [dict(row._mapping) for row in sql_result]
                output.results = results
            except Exception as e:
                logger.error("Error executing generated SQL: %s", str(e))
                output.results = []
                output.explanation += f"\n\n(Error al ejecutar la consulta: {str(e)})"
            
        return output
    except Exception as e:
        logger.error("Error generating SQL: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating SQL: {str(e)}"
        )
