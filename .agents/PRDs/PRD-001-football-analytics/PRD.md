---
id: PRD-001
slug: football-analytics
title: Football Analytics
status: draft
base_branch: main
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
updated: 2026-05-27
---

# PRD-001: Football Analytics

## 1. Executive Summary
Football Analytics es una aplicación web diseñada para democratizar el acceso a estadísticas complejas de fútbol mediante lenguaje natural. Los usuarios pueden realizar preguntas en español (ej. "¿Quiénes son los 5 máximos goleadores de la liga española?") y el sistema traducirá estas inquietudes a consultas SQL precisas y optimizadas.

El objetivo del MVP es proporcionar una interfaz limpia donde el usuario pueda validar la lógica generada por la IA, visualizando el código SQL resultante sin ejecutarlo inicialmente en la base de datos por motivos de seguridad y control pedagógico.

## 2. Mission
Nuestra misión es facilitar la exploración de datos deportivos sin requerir conocimientos técnicos de bases de datos.
- **Simplicidad**: Interfaz intuitiva enfocada en la búsqueda.
- **Transparencia**: Mostrar el SQL generado para fomentar el aprendizaje y la validación.
- **Precisión**: Utilizar modelos de lenguaje avanzados (Gemini) para una traducción fiel del lenguaje natural a SQL.

## 3. Target Users
- **Analistas de fútbol amateur**: Personas que buscan datos específicos para blogs o redes sociales.
- **Estudiantes de SQL**: Usuarios que quieren ver cómo se traducen preguntas complejas a código.
- **Fans curiosos**: Usuarios que desean resolver debates estadísticos rápidamente.

## 4. MVP Scope

### In Scope
- [ ] Interfaz de chat/buscador simple (Frontend React).
- [ ] Backend en FastAPI para procesar solicitudes.
- [ ] Integración con Google Gemini para generación de SQL.
- [ ] Esquema de base de datos relacional (PostgreSQL/SQLite) con tablas de equipos, jugadores, partidos y estadísticas.
- [ ] Panel de visualización de código SQL con resaltado de sintaxis.
- [ ] Traducción de preguntas en español a SQL.

### Out of Scope
- [ ] Ejecución directa de queries en el frontend (por seguridad en MVP).
- [ ] Visualización de resultados de la base de datos en tablas o gráficos.
- [ ] Autenticación de usuarios.
- [ ] Exportación de resultados a Excel/PDF.
- [ ] Historial de consultas persistente (guardado en DB).

## 5. User Stories
- **Como usuario**, quiero escribir una pregunta en español sobre fútbol para que el sistema me genere la consulta SQL necesaria.
- **Como usuario**, quiero ver el código SQL generado de forma clara para entender cómo se consultan los datos.
- **Como desarrollador**, quiero que el sistema use Gemini para que la traducción sea lo más precisa posible.
- **Como administrador**, quiero que las consultas no se ejecuten automáticamente para evitar cargas innecesarias o riesgos de seguridad.

## 6. Core Architecture & Patterns
- **Frontend**: React 19 SPA.
  - Patrón: Declarative Routing con `react-router`.
  - UI: Componentes de `shadcn/ui` para una estética moderna y limpia.
- **Backend**: FastAPI.
  - Patrón: Functional/Declarative approach.
  - IA: `pydantic-ai` para la orquestación del agente.
- **Agente de IA**:
  - Modelo: `google-gla:gemini-1.5-flash`.
  - Contexto: Se le proporcionará el DDL (Data Definition Language) de la base de datos en el system prompt.

## 7. Tools/Features
- **SQL Generator**: Endpoint que recibe texto, llama a Gemini y devuelve un string con el SQL.
- **Syntax Highlighter**: Componente en el frontend para mostrar el código SQL.
- **Database Schema Explorer**: Script o herramienta interna para que la IA conozca las tablas y columnas.

## 8. Technology Stack
- **Frontend**: React 19, Vite, Tailwind CSS v4, shadcn/ui.
- **Backend**: Python 3.10+, FastAPI, Pydantic v2, `pydantic-ai`.
- **LLM**: Google Gemini API via Pydantic AI.
- **Base de Datos**: PostgreSQL (para el esquema de referencia) y SQLite (local dev).

## 9. Security & Configuration
- **API Keys**: Almacenadas en `.env` (no committeadas).
- **Sanitización**: El agente debe ser instruido para generar únicamente sentencias `SELECT`.
- **Validación**: Uso de Pydantic para validar los payloads de entrada y salida.

## 10. API Specification
- `POST /api/v1/generate-sql`:
  - Request: `{ "prompt": string }`
  - Response: `{ "sql": string, "explanation": string }`

## 11. Success Criteria
- [ ] El frontend carga correctamente y muestra el input de búsqueda.
- [ ] Las preguntas en español reciben una respuesta con código SQL válido.
- [ ] El código SQL se visualiza en un panel dedicado con formato legible.
- [ ] El backend no intenta ejecutar la query en la base de datos de producción.

## 12. Implementation Phases
1. **Fase 1: Setup & DB Schema**: Definir el esquema de fútbol y configurar proyectos.
2. **Fase 2: Backend & Agent**: Implementar el agente con Pydantic AI y el endpoint de FastAPI.
3. **Fase 3: Frontend**: Crear la interfaz con React y shadcn.
4. **Fase 4: Integración & Refinamiento**: Conectar front y back, y ajustar el prompt de Gemini.

## 13. Future Considerations
- Habilitar la ejecución de queries con límites (LIMIT 100).
- Gráficos automáticos basados en el resultado de la query.
- Soporte para múltiples ligas y temporadas.

## 14. Risks & Mitigations
- **Alucinaciones de la IA**: Mitigado proporcionando el esquema exacto (DDL) en el prompt.
- **Queries maliciosas**: Mitigado por la instrucción del agente y la no ejecución en el MVP.
- **Latencia de la API**: Uso de streaming o indicadores de carga en el frontend.

## 15. Appendix
- **Skills referenced**: `building-pydantic-ai-agents`, `fastapi-python`, `react-router-declarative-mode`, `shadcn`, `vercel-react-best-practices`.
