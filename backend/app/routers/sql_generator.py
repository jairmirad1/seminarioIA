import logging
from fastapi import APIRouter, HTTPException, status
from app.schemas.ai import SQLGenerationRequest, SQLGenerationResult
from app.services.ai.sql_agent import sql_agent

logger = logging.getLogger("api.routers.sql_generator")

router = APIRouter(tags=["sql-generator"])

@router.post("/generate-sql", response_model=SQLGenerationResult)
async def generate_sql(request: SQLGenerationRequest):
    """
    Generate a SQL SELECT query from a natural language prompt in Spanish.
    """
    logger.info("POST /generate-sql prompt=%s", request.prompt)
    try:
        # Pydantic AI agent.run() is async
        result = await sql_agent.run(request.prompt)
        return result.data
    except Exception as e:
        logger.error("Error generating SQL: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating SQL: {str(e)}"
        )
