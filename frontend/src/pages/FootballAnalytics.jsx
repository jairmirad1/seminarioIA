import { useState, useTransition } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"
import { AlertCircle, Copy, Check } from "lucide-react"
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter"
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism"
import { generateSql } from "@/lib/api"

export default function FootballAnalytics() {
  const [prompt, setPrompt] = useState("")
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [isPending, startTransition] = useTransition()
  const [copied, setCopied] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!prompt.trim()) return

    setError(null)
    setResult(null)
    setCopied(false)

    startTransition(async () => {
      try {
        const data = await generateSql(prompt)
        setResult(data)
      } catch (err) {
        setError(err.message)
      }
    })
  }

  const handleCopy = () => {
    if (result?.sql) {
      navigator.clipboard.writeText(result.sql)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    }
  }

  return (
    <div className="container max-w-4xl mx-auto py-12 px-4">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold tracking-tight mb-4 text-primary">Football Analytics</h1>
        <p className="text-muted-foreground text-lg">
          Pregunta sobre estadísticas de fútbol en español y obtén la consulta SQL optimizada.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="flex flex-col gap-4 mb-12">
        <div className="flex gap-2">
          <Input
            placeholder="Ej. ¿Quiénes son los 5 jugadores con más goles?"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="text-lg py-6 focus-visible:ring-primary"
            disabled={isPending}
          />
          <Button type="submit" size="lg" className="px-8 font-semibold" disabled={isPending}>
            {isPending ? "Generando..." : "Generar SQL"}
          </Button>
        </div>
      </form>

      {error && (
        <Alert variant="destructive" className="mb-8 animate-in fade-in zoom-in-95">
          <AlertCircle className="h-4 w-4" />
          <AlertTitle>Error de Generación</AlertTitle>
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}

      {result && (
        <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
          <Card className="shadow-md border-primary/20">
            <CardHeader className="pb-3">
              <CardTitle className="text-xl">Explicación de la IA</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-foreground leading-relaxed italic">
                "{result.explanation}"
              </p>
            </CardContent>
          </Card>
          
          <Card className="shadow-lg overflow-hidden border-muted-foreground/20">
            <CardHeader className="flex flex-row items-center justify-between pb-3 bg-muted/30">
              <CardTitle className="text-xl">Consulta SQL Generada</CardTitle>
              <Button 
                variant="outline" 
                size="sm" 
                onClick={handleCopy}
                className="h-8 gap-2 transition-all active:scale-95"
              >
                {copied ? <Check className="h-3.5 w-3.5 text-green-500" /> : <Copy className="h-3.5 w-3.5" />}
                {copied ? "Copiado" : "Copiar"}
              </Button>
            </CardHeader>
            <CardContent className="p-0">
              <div className="relative group">
                <SyntaxHighlighter 
                  language="sql" 
                  style={vscDarkPlus}
                  customStyle={{
                    margin: 0,
                    borderRadius: 0,
                    fontSize: "14px",
                    padding: "24px",
                    backgroundColor: "#1e1e1e",
                  }}
                  showLineNumbers={true}
                >
                  {result.sql}
                </SyntaxHighlighter>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  )
}
