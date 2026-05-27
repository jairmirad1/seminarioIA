-- Football Analytics Schema (SQLite)
-- Restored to original structure with Teams, Players, Matches, and Player_Stats

CREATE TABLE equipos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    estadio VARCHAR(100),
    anio_fundacion INTEGER
);

CREATE TABLE jugadores (
    id INTEGER PRIMARY KEY,
    equipo_id INTEGER NOT NULL,
    nombre_completo VARCHAR(100) NOT NULL,
    posicion VARCHAR(50),
    FOREIGN KEY(equipo_id) REFERENCES equipos (id)
);

CREATE TABLE partidos (
    id INTEGER PRIMARY KEY,
    equipo_local_id INTEGER NOT NULL,
    equipo_visitante_id INTEGER NOT NULL,
    fecha DATE NOT NULL,
    goles_local INTEGER NOT NULL,
    goles_visitante INTEGER NOT NULL,
    FOREIGN KEY(equipo_local_id) REFERENCES equipos (id),
    FOREIGN KEY(equipo_visitante_id) REFERENCES equipos (id)
);

CREATE TABLE estadisticas (
    id INTEGER PRIMARY KEY,
    jugador_id INTEGER NOT NULL,
    partido_id INTEGER NOT NULL,
    goles INTEGER NOT NULL DEFAULT 0,
    asistencias INTEGER NOT NULL DEFAULT 0,
    minutos_jugados INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(jugador_id) REFERENCES jugadores (id),
    FOREIGN KEY(partido_id) REFERENCES partidos (id)
);
