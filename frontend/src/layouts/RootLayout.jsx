import { Outlet, NavLink } from "react-router"

const navItems = [
  { label: "Home", to: "/" },
  { label: "Analytics", to: "/analytics" },
  { label: "About", to: "/about" },
  { label: "Dashboard", to: "/dashboard" },
]

export default function RootLayout() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <header className="border-b border-slate-800/80 bg-slate-950/95 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-5 sm:px-6 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-cyan-300/80">World Elite 50</p>
            <h1 className="text-2xl font-semibold tracking-tight text-white sm:text-3xl">Top 50 Jugadores del Mundo</h1>
          </div>

          <nav className="flex flex-wrap items-center gap-3 text-sm font-medium">
            {navItems.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.to === "/"}
                className={({ isActive }) =>
                  `rounded-full px-4 py-2 transition-all duration-200 ${
                    isActive
                      ? "bg-cyan-500 text-slate-950 shadow-lg shadow-cyan-500/20"
                      : "text-slate-300 hover:bg-slate-800/80 hover:text-white"
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </header>

      <main className="mx-auto flex min-h-[calc(100vh-96px)] max-w-7xl flex-col px-4 py-10 sm:px-6 lg:px-8">
        <Outlet />
      </main>
    </div>
  )
}
