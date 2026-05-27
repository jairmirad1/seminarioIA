const API_BASE_URL = "http://localhost:8000/api/v1";

/**
 * Generates a SQL query from a natural language prompt.
 * @param {string} prompt 
 * @returns {Promise<{sql: string, explanation: string}>}
 */
export async function generateSql(prompt) {
  const response = await fetch(`${API_BASE_URL}/generate-sql`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || "Error generating SQL");
  }

  return response.json();
}
