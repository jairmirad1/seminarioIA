-- 1. CREACIÓN DE TABLAS DESDE CERO

DROP TABLE IF EXISTS estadisticas;
DROP TABLE IF EXISTS jugadores;
DROP TABLE IF EXISTS equipos;
DROP TABLE IF EXISTS partidos; -- No longer used in this schema but cleaning up

CREATE TABLE equipos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE jugadores (
    id INTEGER PRIMARY KEY,
    equipo_id INTEGER NOT NULL,
    nombre_completo VARCHAR(100) NOT NULL,
    edad INTEGER NOT NULL,
    posicion VARCHAR(50),
    valor_mercado_millones DECIMAL(10,2),
    FOREIGN KEY(equipo_id) REFERENCES equipos (id)
);

CREATE TABLE estadisticas (
    jugador_id INTEGER PRIMARY KEY,
    alineaciones INTEGER NOT NULL DEFAULT 0,
    goles INTEGER NOT NULL DEFAULT 0,
    asistencias INTEGER NOT NULL DEFAULT 0,
    tarjetas_amarillas INTEGER NOT NULL DEFAULT 0,
    tarjetas_rojas INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY(jugador_id) REFERENCES jugadores (id)
);

-- 2. INSERCIÓN DE EQUIPOS (Basado en los escudos de las imágenes)

INSERT INTO equipos (id, nombre) VALUES
(1, 'FC Barcelona'),
(2, 'Manchester City FC'),
(3, 'Real Madrid CF'),
(4, 'FC Bayern Munchen'),
(5, 'Arsenal FC'),
(6, 'Chelsea FC'),
(7, 'Paris Saint-Germain'),
(8, 'Liverpool FC'),
(9, 'RB Leipzig'),
(10, 'Eintracht Frankfurt'),
(11, 'Atletico de Madrid'),
(12, 'Inter de Milan'),
(13, 'Real Sociedad'),
(14, 'Aston Villa'),
(15, 'Manchester United'),
(16, 'Newcastle United'),
(17, 'Juventus FC'),
(18, 'Galatasaray SK');

-- 3. INSERCIÓN DE LOS 50 JUGADORES 
-- (Con sus edades, posiciones y valores de mercado en millones exactos)

INSERT INTO jugadores (id, equipo_id, nombre_completo, edad, posicion, valor_mercado_millones) VALUES
(1, 1, 'Lamine Yamal', 18, 'Extremo derecho', 200.00),
(2, 2, 'Erling Haaland', 25, 'Delantero centro', 200.00),
(3, 3, 'Kylian Mbappe', 27, 'Delantero centro', 200.00),
(4, 1, 'Pedri', 23, 'Mediocentro', 150.00),
(5, 4, 'Michael Olise', 24, 'Extremo derecho', 150.00),
(6, 3, 'Vinicius Junior', 25, 'Extremo izquierdo', 150.00),
(7, 3, 'Jude Bellingham', 22, 'Mediocentro ofensivo', 140.00),
(8, 5, 'Bukayo Saka', 24, 'Extremo derecho', 120.00),
(9, 3, 'Federico Valverde', 27, 'Mediocentro', 120.00),
(10, 5, 'Declan Rice', 27, 'Mediocentro', 120.00),
(11, 6, 'Moises Caicedo', 24, 'Pivote', 110.00),
(12, 7, 'Joao Neves', 21, 'Mediocentro', 110.00),
(13, 8, 'Florian Wirtz', 23, 'Mediocentro ofensivo', 110.00),
(14, 6, 'Cole Palmer', 24, 'Mediocentro ofensivo', 110.00),
(15, 7, 'Vitinha', 26, 'Pivote', 110.00),
(16, 1, 'Fermin Lopez', 23, 'Mediocentro ofensivo', 100.00),
(17, 4, 'Jamal Musiala', 23, 'Mediocentro ofensivo', 100.00),
(18, 8, 'Dominik Szoboszlai', 25, 'Mediocentro ofensivo', 100.00),
(19, 8, 'Alexander Isak', 26, 'Delantero centro', 100.00),
(20, 7, 'Ousmane Dembele', 29, 'Delantero centro', 100.00),
(21, 9, 'Yan Diomande', 19, 'Extremo izquierdo', 90.00),
(22, 7, 'Desire Doue', 20, 'Extremo derecho', 90.00),
(23, 3, 'Arda Guler', 21, 'Mediocentro ofensivo', 90.00),
(24, 4, 'Aleksandar Pavlovic', 22, 'Pivote', 90.00),
(25, 10, 'Hugo Ekitike', 23, 'Delantero centro', 90.00),
(26, 6, 'Enzo Fernandez', 25, 'Mediocentro', 90.00),
(27, 11, 'Julian Alvarez', 26, 'Delantero centro', 90.00),
(28, 7, 'Khvicha Kvaratskhelia', 25, 'Extremo izquierdo', 90.00),
(29, 5, 'William Saliba', 25, 'Defensa central', 90.00),
(30, 8, 'Ryan Gravenberch', 24, 'Pivote', 90.00),
(31, 12, 'Lautaro Martinez', 28, 'Delantero centro', 85.00),
(32, 6, 'Estevao', 19, 'Extremo derecho', 80.00),
(33, 1, 'Pau Cubarsi', 19, 'Defensa central', 80.00),
(34, 13, 'Nico Paz', 21, 'Mediocentro ofensivo', 80.00),
(35, 8, 'Alexis Mac Allister', 27, 'Mediocentro', 80.00),
(36, 14, 'Morgan Rogers', 23, 'Mediocentro ofensivo', 80.00),
(37, 5, 'Martin Zubimendi', 27, 'Pivote', 80.00),
(38, 15, 'Bryan Mbeumo', 26, 'Extremo derecho', 80.00),
(39, 1, 'Raphinha', 29, 'Extremo izquierdo', 80.00),
(40, 2, 'Phil Foden', 26, 'Mediocentro ofensivo', 80.00),
(41, 7, 'Achraf Hakimi', 27, 'Lateral derecho', 80.00),
(42, 16, 'Sandro Tonali', 26, 'Pivote', 80.00),
(43, 17, 'Kenan Yildiz', 21, 'Extremo izquierdo', 75.00),
(44, 6, 'Joao Pedro', 24, 'Delantero centro', 75.00),
(45, 7, 'Nuno Mendes', 23, 'Lateral izquierdo', 75.00),
(46, 2, 'Antoine Semenyo', 26, 'Extremo derecho', 75.00),
(47, 16, 'Bruno Guimaraes', 28, 'Mediocentro', 75.00),
(48, 5, 'Gabriel', 28, 'Defensa central', 75.00),
(49, 3, 'Aurelien Tchouameni', 26, 'Pivote', 75.00),
(50, 18, 'Victor Osimhen', 27, 'Delantero centro', 75.00);

-- 4. INSERCIÓN DE LAS ESTADÍSTICAS TOTALES
-- (Alineaciones, goles, asistencias, tarjetas amarillas y rojas según la imagen)

INSERT INTO estadisticas (jugador_id, alineaciones, goles, asistencias, tarjetas_amarillas, tarjetas_rojas) VALUES
(1, 25, 15, 7, 3, 0),
(2, 28, 13, 5, 2, 0),
(3, 20, 13, 2, 3, 0),
(4, 24, 0, 6, 1, 0),
(5, 27, 12, 17, 7, 0),
(6, 29, 17, 5, 7, 0),
(7, 20, 3, 1, 3, 0),
(8, 23, 4, 4, 1, 0),
(9, 27, 9, 9, 2, 1),
(10, 28, 3, 4, 3, 0),
(11, 27, 1, 0, 8, 0),
(12, 22, 1, 2, 0, 0),
(13, 26, 6, 4, 0, 0),
(14, 24, 7, 3, 6, 0),
(15, 26, 2, 2, 1, 0),
(16, 30, 6, 13, 4, 0),
(17, 24, 5, 6, 2, 0),
(18, 29, 8, 7, 5, 1),
(19, 6, 1, 0, 0, 0),
(20, 25, 15, 7, 0, 0),
(21, 20, 6, 6, 0, 0),
(22, 28, 8, 7, 1, 0),
(23, 26, 3, 7, 0, 0),
(24, 23, 3, 1, 2, 0),
(25, 20, 6, 4, 0, 0),
(26, 28, 9, 5, 9, 0),
(27, 26, 9, 4, 0, 0),
(28, 26, 13, 5, 3, 0),
(29, 28, 1, 0, 2, 0),
(30, 29, 2, 3, 4, 0),
(31, 19, 9, 3, 2, 0),
(32, 13, 3, 3, 3, 0),
(33, 27, 1, 0, 3, 1),
(34, 23, 7, 2, 3, 0),
(35, 30, 4, 5, 7, 0),
(36, 29, 7, 7, 4, 0),
(37, 32, 3, 0, 2, 0),
(38, 17, 5, 2, 1, 0),
(39, 19, 14, 5, 3, 0),
(40, 26, 0, 3, 1, 0),
(41, 17, 1, 6, 2, 1),
(42, 27, 3, 3, 5, 0),
(43, 24, 4, 3, 4, 0),
(44, 26, 13, 5, 3, 0),
(45, 22, 2, 3, 1, 0),
(46, 29, 12, 3, 3, 0),
(47, 14, 3, 3, 5, 0),
(48, 31, 1, 2, 3, 0),
(49, 26, 2, 1, 6, 0),
(50, 17, 10, 8, 7, 0);
