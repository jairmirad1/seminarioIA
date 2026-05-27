-- Football Analytics Schema (PostgreSQL Dialect)
-- Generated automatically for AI Agent context

CREATE TABLE equipos (
	id SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	ciudad VARCHAR(100), 
	estadio VARCHAR(100), 
	PRIMARY KEY (id)
);

CREATE TABLE jugadores (
	id SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	posicion VARCHAR(50), 
	numero_camiseta INTEGER, 
	equipo_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(equipo_id) REFERENCES equipos (id)
);

CREATE TABLE partidos (
	id SERIAL NOT NULL, 
	equipo_local_id INTEGER NOT NULL, 
	equipo_visitante_id INTEGER NOT NULL, 
	fecha DATE NOT NULL, 
	goles_local INTEGER NOT NULL, 
	goles_visitante INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(equipo_local_id) REFERENCES equipos (id), 
	FOREIGN KEY(equipo_visitante_id) REFERENCES equipos (id)
);

CREATE TABLE estadisticas (
	id SERIAL NOT NULL, 
	partido_id INTEGER NOT NULL, 
	jugador_id INTEGER NOT NULL, 
	goles INTEGER NOT NULL, 
	asistencias INTEGER NOT NULL, 
	tarjetas_amarillas INTEGER NOT NULL, 
	tarjetas_rojas INTEGER NOT NULL, 
	minutos_jugados INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(partido_id) REFERENCES partidos (id), 
	FOREIGN KEY(jugador_id) REFERENCES jugadores (id)
);