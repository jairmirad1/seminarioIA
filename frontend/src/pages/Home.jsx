import { NavLink } from "react-router"
import { ArrowRight } from "lucide-react"

export default function Home() {
  return (
    <div className="grid gap-10 lg:grid-cols-[1.05fr_0.95fr]">
      <section className="space-y-8 rounded-[2rem] border border-white/10 bg-white/5 p-10 shadow-[0_30px_120px_-50px_rgba(14,165,233,0.45)] backdrop-blur-xl">
        <div className="max-w-2xl space-y-5">
          <span className="inline-flex rounded-full bg-cyan-500/15 px-4 py-1 text-sm font-semibold text-cyan-200">
            Lanza tu análisis de fútbol con SQL generado por IA
          </span>
          <h2 className="text-4xl font-semibold tracking-tight text-white sm:text-5xl">
            Transforma preguntas en consultas SQL precisas para tu base de datos de fútbol.
          </h2>
          <p className="text-slate-300 leading-8 text-lg">
            Usa lenguaje natural en español para obtener sentencias SELECT optimizadas. Ideal para analistas, dashboards y equipos que necesitan respuestas rápidas sin escribir SQL manualmente.
          </p>
          <div className="flex flex-col gap-4 sm:flex-row">
            <NavLink
              to="/analytics"
              className="inline-flex items-center justify-center rounded-full bg-cyan-500 px-6 py-3 text-sm font-semibold text-slate-950 transition hover:bg-cyan-400"
            >
              Ir a Analytics
              <ArrowRight className="ml-2 h-4 w-4" />
            </NavLink>
            <NavLink
              to="/about"
              className="inline-flex items-center justify-center rounded-full border border-slate-700/90 px-6 py-3 text-sm font-semibold text-slate-100 transition hover:border-slate-500"
            >
              Aprende más
            </NavLink>
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          <article className="rounded-3xl border border-white/10 bg-slate-950/80 p-6 text-slate-100 shadow-xl shadow-slate-950/30">
            <p className="text-xs uppercase tracking-[0.32em] text-cyan-300/70">Automatización</p>
            <h3 className="mt-3 text-xl font-semibold">Menos horas, más insights</h3>
            <p className="mt-2 text-slate-400">Convierte preguntas complejas en SQL sin conocer el esquema a fondo.</p>
          </article>
          <article className="rounded-3xl border border-white/10 bg-slate-950/80 p-6 text-slate-100 shadow-xl shadow-slate-950/30">
            <p className="text-xs uppercase tracking-[0.32em] text-cyan-300/70">Precisión</p>
            <h3 className="mt-3 text-xl font-semibold">Consultas seguras</h3>
            <p className="mt-2 text-slate-400">Solo se generan SELECTs válidos dentro del esquema definido.</p>
          </article>
        </div>
      </section>

      <aside className="space-y-6 rounded-[2rem] border border-white/10 bg-slate-950/80 p-8 shadow-[0_35px_90px_-40px_rgba(15,23,42,0.9)] backdrop-blur-xl">
        <div className="rounded-3xl bg-slate-900/80 p-6 text-slate-100 shadow-inner shadow-slate-950/30">
          <p className="text-sm uppercase tracking-[0.35em] text-cyan-300/80">Interfaz limpia</p>
          <h3 className="mt-4 text-2xl font-semibold">Diseñada para analistas</h3>
          <p className="mt-3 text-slate-400 leading-7">
            Accede rápido a la generación de SQL, copia resultados y obtén explicaciones claras en español.
          </p>
        </div>

        <div className="grid gap-4">
          <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-5">
            <p className="text-xs uppercase tracking-[0.35em] text-slate-400">Flujo recomendado</p>
            <ol className="mt-4 space-y-3 text-slate-300">
              <li>1. Ingresa tu pregunta en español.</li>
              <li>2. Genera la consulta SQL.</li>
              <li>3. Copia y usa el resultado en tu dashboard.</li>
            </ol>
          </div>
          <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-5">
            <p className="text-xs uppercase tracking-[0.35em] text-slate-400">Ejemplo</p>
            <p className="mt-3 text-slate-300">«¿Cuáles son los 5 jugadores con más goles?»</p>
          </div>
        </div>
      </aside>
    </div>
  )
}
