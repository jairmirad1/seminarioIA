import { useState, useTransition, useRef, useEffect } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"
import { AlertCircle, Copy, Check, Send, User, Bot } from "lucide-react"
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter"
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism"
import { generateSql } from "@/lib/api"
import { cn } from "@/lib/utils"

export default function FootballAnalytics() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "¡Hola! Soy tu Scout de Fútbol con IA. Puedo ayudarte a analizar a los 50 mejores jugadores del mundo usando SQL. ¿Qué te gustaría saber hoy?",
    },
  ])
  const [input, setInput] = useState("")
  const [isPending, startTransition] = useTransition()
  const [error, setError] = useState(null)
  const [copiedIndex, setCopiedIndex] = useState(null)
  
  const scrollRef = useRef(null)

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [messages, isPending])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!input.trim() || isPending) return

    const userMessage = { role: "user", content: input }
    const updatedMessages = [...messages, userMessage]
    
    setMessages(updatedMessages)
    setInput("")
    setError(null)

    startTransition(async () => {
      try {
        // Sanitize messages to only include role and content
        const sanitizedMessages = updatedMessages.map(({ role, content }) => ({ role, content }))
        
        // Send the full history (including the new user message)
        const response = await generateSql(sanitizedMessages)
        
        const assistantMessage = {
          role: "assistant",
          content: response.explanation,
          sql: response.sql,
          results: response.results,
        }
        
        setMessages((prev) => [...prev, assistantMessage])
      } catch (err) {
        setError(err.message)
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: "Lo siento, hubo un error al procesar tu solicitud. " + err.message, isError: true }
        ])
      }
    })
  }

  const handleCopy = (sql, index) => {
    navigator.clipboard.writeText(sql)
    setCopiedIndex(index)
    setTimeout(() => setCopiedIndex(null), 2000)
  }

  return (
    <div className="mx-auto grid max-w-6xl gap-8 lg:grid-cols-[1fr_320px] lg:gap-10 h-[calc(100vh-160px)]">
      <section className="flex flex-col min-w-0 rounded-[2rem] border border-white/10 bg-slate-950/85 shadow-[0_35px_90px_-40px_rgba(15,23,42,0.9)] backdrop-blur-xl overflow-hidden">
        {/* Chat Header */}
        <div className="p-6 border-b border-white/5 bg-slate-900/40 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-cyan-500/10 text-cyan-400 ring-1 ring-cyan-500/20">
              <Bot className="h-5 w-5" />
            </div>
            <div>
              <h1 className="text-xl font-semibold text-white">AI Football Scout</h1>
              <p className="text-xs text-slate-400">Conversación en tiempo real</p>
            </div>
          </div>
          <div className="hidden sm:block text-right">
            <div className="inline-flex items-center gap-2 rounded-full bg-emerald-500/10 px-3 py-1 text-[10px] font-medium text-emerald-400 ring-1 ring-emerald-500/20">
              <span className="h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse" />
              Base de Datos Conectada
            </div>
          </div>
        </div>

        {/* Messages Area */}
        <div 
          ref={scrollRef}
          className="flex-1 overflow-y-auto p-6 space-y-6 scroll-smooth no-scrollbar"
        >
          {messages.map((msg, idx) => (
            <div 
              key={idx} 
              className={cn(
                "flex w-full animate-in fade-in slide-in-from-bottom-2 duration-300 min-w-0",
                msg.role === "user" ? "justify-end" : "justify-start"
              )}
            >
              <div className={cn(
                "flex max-w-[85%] gap-3 min-w-0 overflow-hidden",
                msg.role === "user" ? "flex-row-reverse" : "flex-row"
              )}>
                <div className={cn(
                  "flex h-8 w-8 shrink-0 select-none items-center justify-center rounded-full border text-[10px] font-bold",
                  msg.role === "user" 
                    ? "bg-slate-800 border-slate-700 text-slate-200" 
                    : "bg-cyan-500/20 border-cyan-500/30 text-cyan-400"
                )}>
                  {msg.role === "user" ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
                </div>
                
                <div className="space-y-3 min-w-0 flex-1 overflow-hidden">
                  <div className={cn(
                    "rounded-2xl px-4 py-3 text-sm sm:text-base shadow-lg break-words whitespace-normal max-w-full",
                    msg.role === "user" 
                      ? "bg-cyan-600 text-white rounded-tr-none" 
                      : msg.isError 
                        ? "bg-red-500/10 border border-red-500/20 text-red-200 rounded-tl-none"
                        : "bg-slate-900 border border-slate-800 text-slate-200 rounded-tl-none"
                  )}>
                    {msg.content}
                  </div>

                  {msg.role === "assistant" && msg.sql && (
                    <div className="space-y-4 animate-in zoom-in-95 duration-500 delay-150 fill-mode-both max-w-full overflow-hidden">
                      {/* SQL Code */}
                      <div className="rounded-xl border border-slate-800/80 bg-slate-950 overflow-hidden max-w-full">
                        <div className="flex items-center justify-between bg-slate-900/80 px-4 py-2 border-b border-slate-800/50">
                          <span className="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Consulta SQL</span>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={() => handleCopy(msg.sql, idx)}
                            className="h-7 px-2 text-xs text-slate-400 hover:text-white hover:bg-white/5"
                          >
                            {copiedIndex === idx ? <Check className="h-3 w-3 text-emerald-400" /> : <Copy className="h-3 w-3" />}
                          </Button>
                        </div>
                        <div className="p-0 bg-[#111827] max-w-full overflow-hidden">
                          <SyntaxHighlighter
                            language="sql"
                            style={vscDarkPlus}
                            wrapLongLines={true}
                            customStyle={{
                              margin: 0,
                              padding: "16px",
                              fontSize: "12px",
                              backgroundColor: "transparent",
                              width: "100%",
                            }}
                          >
                            {msg.sql}
                          </SyntaxHighlighter>
                        </div>
                      </div>

                      {/* Results Table */}
                      {msg.results && msg.results.length > 0 && (
                        <div className="rounded-xl border border-slate-800/80 bg-slate-900/50 overflow-hidden max-w-full">
                          <div className="bg-slate-950/40 px-3 py-1.5 border-b border-slate-800/50">
                             <span className="text-[9px] uppercase tracking-wider text-slate-400 font-semibold">Resultados ({msg.results.length})</span>
                          </div>
                          <div className="max-w-full overflow-hidden">
                            <table className="w-full table-fixed text-left text-sm text-slate-300 border-collapse">
                              <thead className="bg-slate-950/50">
                                <tr>
                                  {Object.keys(msg.results[0]).map((key) => (
                                    <th key={key} className="px-2 py-1 font-semibold uppercase tracking-wider border-b border-slate-800/50 text-cyan-400/70 break-words whitespace-normal text-sm">
                                      {key}
                                    </th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody className="divide-y divide-slate-800/30">
                                {msg.results.map((row, i) => (
                                  <tr key={i} className="hover:bg-white/5 transition-colors">
                                    {Object.values(row).map((val, j) => (
                                      <td key={j} className="px-2 py-1.5 break-words whitespace-normal text-sm">
                                        {val !== null ? String(val) : <span className="text-slate-600">null</span>}
                                      </td>
                                    ))}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
          {isPending && (
            <div className="flex justify-start animate-pulse">
              <div className="flex gap-3">
                <div className="flex h-8 w-8 items-center justify-center rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
                  <Bot className="h-4 w-4" />
                </div>
                <div className="bg-slate-900 border border-slate-800 text-slate-400 rounded-2xl rounded-tl-none px-4 py-3 text-sm">
                  Analizando datos...
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="p-6 border-t border-white/5 bg-slate-900/40 shrink-0">
          <form onSubmit={handleSubmit} className="relative group">
            <Input
              placeholder="Pregunta sobre los mejores jugadores..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="pr-14 py-6 bg-slate-950 border-slate-800 focus-visible:ring-cyan-500/50 rounded-2xl text-base"
              disabled={isPending}
            />
            <Button 
              type="submit" 
              size="icon" 
              disabled={!input.trim() || isPending}
              className={cn(
                "absolute right-2 top-1/2 -translate-y-1/2 h-10 w-10 rounded-xl transition-all duration-300",
                input.trim() ? "bg-cyan-500 text-slate-950 hover:bg-cyan-400 shadow-[0_0_20px_rgba(6,182,212,0.3)]" : "bg-slate-800 text-slate-500"
              )}
            >
              <Send className="h-5 w-5" />
            </Button>
          </form>
          <p className="mt-3 text-center text-[10px] text-slate-500 uppercase tracking-widest">
            Usa lenguaje natural para consultar la base de datos de fútbol
          </p>
        </div>
      </section>

      {/* Sidebar */}
      <aside className="hidden lg:flex flex-col gap-6">
        <div className="rounded-3xl border border-white/10 bg-slate-950/80 p-6 shadow-xl">
          <p className="text-xs font-bold uppercase tracking-[0.2em] text-cyan-400/80 mb-4">Contexto de IA</p>
          <div className="space-y-4">
            <div className="p-3 rounded-2xl bg-slate-900/50 border border-slate-800/50">
              <p className="text-xs text-slate-300 leading-relaxed">
                Este chat mantiene el historial de tus preguntas para permitir análisis profundos y comparativos.
              </p>
            </div>
            <div className="space-y-2">
              <p className="text-[10px] uppercase tracking-wider text-slate-500 font-bold px-1">Ejemplos de seguimiento</p>
              <button 
                onClick={() => setInput("¿Quiénes son los delanteros?")}
                className="w-full text-left p-2 text-xs rounded-xl hover:bg-white/5 text-slate-400 hover:text-cyan-300 transition-colors border border-transparent hover:border-cyan-500/20"
              >
                1. "¿Quiénes son los delanteros?"
              </button>
              <button 
                onClick={() => setInput("Ahora filtra solo a los de la Premier League")}
                className="w-full text-left p-2 text-xs rounded-xl hover:bg-white/5 text-slate-400 hover:text-cyan-300 transition-colors border border-transparent hover:border-cyan-500/20"
              >
                2. "Ahora filtra solo a los de la Premier League"
              </button>
            </div>
          </div>
        </div>

        <div className="rounded-3xl border border-white/10 bg-slate-950/80 p-6 shadow-xl flex-1">
          <p className="text-xs font-bold uppercase tracking-[0.2em] text-slate-400 mb-4">Tablas Disponibles</p>
          <ul className="space-y-3">
            {['equipos', 'jugadores', 'partidos', 'estadisticas'].map(table => (
              <li key={table} className="flex items-center gap-2 text-xs text-slate-400">
                <span className="h-1.5 w-1.5 rounded-full bg-slate-700" />
                <code className="bg-slate-900 px-2 py-0.5 rounded text-cyan-300/70">{table}</code>
              </li>
            ))}
          </ul>
        </div>
      </aside>
    </div>
  )
}
