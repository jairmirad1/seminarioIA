import os
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql
from app.models.football import Equipo, Jugador, Partido, Estadistica

def generate_ddl():
    tables = [Equipo.__table__, Jugador.__table__, Partido.__table__, Estadistica.__table__]
    ddl_statements = []
    
    for table in tables:
        # Generate PostgreSQL compatible DDL as a reference for the AI Agent
        ddl = str(CreateTable(table).compile(dialect=postgresql.dialect()))
        ddl_statements.append(ddl.strip() + ";")
        
    # Path relative to backend/ directory
    output_path = os.path.join("app", "models", "football_schema.sql")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("-- Football Analytics Schema (PostgreSQL Dialect)\n")
        f.write("-- Generated automatically for AI Agent context\n\n")
        f.write("\n\n".join(ddl_statements))
    
    print(f"DDL generated at {output_path}")

if __name__ == "__main__":
    generate_ddl()
