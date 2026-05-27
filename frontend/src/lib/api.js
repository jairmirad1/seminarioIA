const API_BASE_URL = "http://127.0.0.1:8000/api/v1";

/**
 * Generates a SQL query from a conversational history.
 * @param {Array<{role: string, content: string}>} messages 
 * @returns {Promise<{sql: string, explanation: string, results?: Array<Object>}>}
 */
export async function generateSql(messages) {
  const response = await fetch(`${API_BASE_URL}/generate-sql`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ messages }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    let errorMessage = "Error generating SQL";
    
    if (errorData.detail) {
      if (Array.isArray(errorData.detail)) {
        errorMessage = errorData.detail.map(err => `${err.loc.join('.')}: ${err.msg}`).join(', ');
      } else if (typeof errorData.detail === 'string') {
        errorMessage = errorData.detail;
      }
    }
    
    throw new Error(errorMessage);
  }

  return response.json();
}
