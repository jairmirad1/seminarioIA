import { useState, useTransition } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { generateSql } from "@/lib/api"

export default function FootballAnalytics() {
  const [prompt, setPrompt] = useState("")
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [isPending, startTransition] = useTransition()

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!prompt.trim()) return

    setError(null)
    setResult(null)

    startTransition(async () => {
      try {
        const data = await generateSql(prompt)
        setResult(data)
      } catch (err) {
        setError(err.message)
      }
    })
  }

  return (
    <div className="container max-w-4xl mx-auto py-12 px-4">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold tracking-tight mb-4">Football Analytics</h1>
        <p className="text-muted-foreground text-lg">
          Pregunta sobre estadísticas de fútbol en español y obtén la consulta SQL.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col gap-4 mb-12">
        <div className="flex gap-2">
          <Input
            placeholder="Ej. ¿Quiénes son los 5 jugadores con más goles?"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="text-lg py-6"
            disabled={isPending}
          />
          <Button type="submit" size="lg" className="px-8" disabled={isPending}>
            {isPending ? "Generando..." : "Generar SQL"}
          </Button>
        </div>
      </form>

      {error && (
        <div className="p-4 border border-destructive/50 bg-destructive/10 text-destructive rounded-lg mb-8">
          <p className="font-semibold">Error</p>
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
          <div className="p-6 border rounded-xl bg-card">
            <h2 className="text-xl font-semibold mb-4">Explicación</h2>
            <p className="text-muted-foreground">{result.explanation}</p>
          </div>
          
          <div className="p-6 border rounded-xl bg-muted overflow-hidden">
            <h2 className="text-xl font-semibold mb-4">Consulta SQL</h2>
            <pre className="p-4 bg-background rounded-lg border overflow-x-auto text-sm font-mono">
              <code>{result.sql}</code>
            </pre>
          </div>
        </div>
      )}
    </div>
  )
}
