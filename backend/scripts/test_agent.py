import asyncio
import os
from app.services.ai.sql_agent import sql_agent

async def test_agent():
    print("Testing SQL Generation Agent...")
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Warning: GOOGLE_API_KEY not found in environment.")
        # We don't exit, maybe it's set via other means or we just want to see the error
    
    prompts = [
        "¿Quiénes son los 3 jugadores más valiosos?",
        "Lista los jugadores menores de 21 años con su equipo y valor",
        "Dime el total de goles y asistencias de Lamine Yamal",
        "¿Qué equipo tiene más jugadores en esta lista?",
        "Muestra los jugadores con más tarjetas rojas"
    ]
    
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        try:
            # run_sync is available in Pydantic AI
            result = sql_agent.run_sync(prompt)
            print(f"SQL: {result.data.sql}")
            print(f"Explicación: {result.data.explanation}")
        except Exception as e:
            print(f"Error running agent: {e}")

if __name__ == "__main__":
    asyncio.run(test_agent())
