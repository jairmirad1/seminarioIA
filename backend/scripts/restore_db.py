import sqlite3
import os

def restore_and_populate():
    db_path = os.path.join(os.path.dirname(__file__), "..", "app.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Drop and recreate tables based on the new schema
    cursor.execute("DROP TABLE IF EXISTS estadisticas")
    cursor.execute("DROP TABLE IF EXISTS partidos")
    cursor.execute("DROP TABLE IF EXISTS jugadores")
    cursor.execute("DROP TABLE IF EXISTS equipos")

    cursor.execute("""
    CREATE TABLE equipos (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        estadio VARCHAR(100),
        anio_fundacion INTEGER
    )
    """)
    cursor.execute("""
    CREATE TABLE jugadores (
        id INTEGER PRIMARY KEY,
        equipo_id INTEGER NOT NULL,
        nombre_completo VARCHAR(100) NOT NULL,
        posicion VARCHAR(50),
        FOREIGN KEY(equipo_id) REFERENCES equipos (id)
    )
    """)
    cursor.execute("""
    CREATE TABLE partidos (
        id INTEGER PRIMARY KEY,
        equipo_local_id INTEGER NOT NULL,
        equipo_visitante_id INTEGER NOT NULL,
        fecha DATE NOT NULL,
        goles_local INTEGER NOT NULL,
        goles_visitante INTEGER NOT NULL,
        FOREIGN KEY(equipo_local_id) REFERENCES equipos (id),
        FOREIGN KEY(equipo_visitante_id) REFERENCES equipos (id)
    )
    """)
    cursor.execute("""
    CREATE TABLE estadisticas (
        id INTEGER PRIMARY KEY,
        jugador_id INTEGER NOT NULL,
        partido_id INTEGER NOT NULL,
        goles INTEGER NOT NULL DEFAULT 0,
        asistencias INTEGER NOT NULL DEFAULT 0,
        minutos_jugados INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(jugador_id) REFERENCES jugadores (id),
        FOREIGN KEY(partido_id) REFERENCES partidos (id)
    )
    """)

    # 2. Populate Teams
    teams = [
        (1, 'Manchester City', 'Etihad Stadium', 1880), (2, 'Real Madrid', 'Santiago Bernabéu', 1902),
        (3, 'Bayern Múnich', 'Allianz Arena', 1900), (4, 'FC Barcelona', 'Camp Nou', 1899),
        (5, 'Liverpool', 'Anfield', 1892), (6, 'Inter de Milán', 'San Siro', 1908),
        (7, 'Arsenal', 'Emirates Stadium', 1886), (8, 'Tottenham', 'Tottenham Hotspur Stadium', 1882),
        (9, 'AC Milan', 'San Siro', 1899), (10, 'Galatasaray', 'Rams Park', 1905),
        (11, 'Atlético de Madrid', 'Cívitas Metropolitano', 1903), (12, 'Newcastle', 'St. James\' Park', 1892),
        (13, 'Sporting CP', 'Estádio José Alvalade', 1906), (14, 'Napoli', 'Stadio Diego Armando Maradona', 1926),
        (15, 'PSG', 'Parc des Princes', 1970), (16, 'Al-Nassr', 'Al-Awwal Park', 1955),
        (17, 'Inter Miami', 'Chase Stadium', 2018), (18, 'Bayer Leverkusen', 'BayArena', 1904),
        (19, 'Chelsea', 'Stamford Bridge', 1905), (20, 'Manchester United', 'Old Trafford', 1878)
    ]
    cursor.executemany("INSERT INTO equipos (id, nombre, estadio, anio_fundacion) VALUES (?, ?, ?, ?)", teams)

    # 3. Populate Matches
    cursor.execute("INSERT INTO partidos (id, equipo_local_id, equipo_visitante_id, fecha, goles_local, goles_visitante) VALUES (1, 1, 2, '2026-05-27', 0, 0)")

    # 4. Populate Players
    players = [
        (1, 1, 'Erling Haaland', 'Delantero'), (2, 2, 'Kylian Mbappé', 'Delantero'), (3, 3, 'Harry Kane', 'Delantero'), (4, 2, 'Vinícius Júnior', 'Delantero'), (5, 4, 'Robert Lewandowski', 'Delantero'), (6, 5, 'Mohamed Salah', 'Delantero'), (7, 6, 'Lautaro Martínez', 'Delantero'), (8, 4, 'Lamine Yamal', 'Delantero'), (9, 7, 'Bukayo Saka', 'Delantero'), (10, 2, 'Rodrygo Goes', 'Delantero'), (11, 1, 'Phil Foden', 'Delantero'), (12, 8, 'Heung-min Son', 'Delantero'), (13, 9, 'Rafael Leão', 'Delantero'), (14, 10, 'Victor Osimhen', 'Delantero'), (15, 11, 'Antoine Griezmann', 'Delantero'), (16, 12, 'Alexander Isak', 'Delantero'), (17, 13, 'Viktor Gyökeres', 'Delantero'), (18, 14, 'Khvicha Kvaratskhelia', 'Delantero'), (19, 15, 'Ousmane Dembélé', 'Delantero'), (20, 5, 'Luis Díaz', 'Delantero'), (21, 11, 'Julián Álvarez', 'Delantero'), (22, 16, 'Cristiano Ronaldo', 'Delantero'), (23, 17, 'Lionel Messi', 'Delantero'),
        (24, 2, 'Jude Bellingham', 'Mediocampista'), (25, 1, 'Rodri Hernández', 'Mediocampista'), (26, 1, 'Kevin De Bruyne', 'Mediocampista'), (27, 18, 'Florian Wirtz', 'Mediocampista'), (28, 3, 'Jamal Musiala', 'Mediocampista'), (29, 2, 'Federico Valverde', 'Mediocampista'), (30, 7, 'Martin Ødegaard', 'Mediocampista'), (31, 7, 'Declan Rice', 'Mediocampista'), (32, 19, 'Cole Palmer', 'Mediocampista'), (33, 20, 'Bruno Fernandes', 'Mediocampista'), (34, 1, 'Ilkay Gündogan', 'Mediocampista'), (35, 5, 'Alexis Mac Allister', 'Mediocampista'), (36, 2, 'Aurélien Tchouaméni', 'Mediocampista'), (37, 1, 'Bernardo Silva', 'Mediocampista'), (38, 6, 'Hakan Çalhanoglu', 'Mediocampista'), (39, 4, 'Pedri González', 'Mediocampista'), (40, 4, 'Gavi (Páez)', 'Mediocampista'), (41, 2, 'Luka Modric', 'Mediocampista'),
        (42, 5, 'Virgil van Dijk', 'Defensor'), (43, 2, 'Antonio Rüdiger', 'Defensor'), (44, 7, 'William Saliba', 'Defensor'), (45, 1, 'Rúben Dias', 'Defensor'), (46, 5, 'Trent Alexander-Arnold', 'Defensor'), (47, 15, 'Achraf Hakimi', 'Defensor'), (48, 3, 'Alfonso Davies', 'Defensor'), (49, 9, 'Theo Hernández', 'Defensor'), (50, 1, 'Kyle Walker', 'Defensor'), (51, 6, 'Alessandro Bastoni', 'Defensor'), (52, 1, 'John Stones', 'Defensor'), (53, 4, 'Ronald Araújo', 'Defensor'), (54, 7, 'Gabriel Magalhães', 'Defensor')
    ]
    cursor.executemany("INSERT INTO jugadores (id, equipo_id, nombre_completo, posicion) VALUES (?, ?, ?, ?)", players)

    # 5. Populate Stats
    stats = [
        (1, 1, 1, 40, 8, 3100), (2, 2, 1, 35, 10, 2900), (3, 3, 1, 38, 12, 3050), (4, 4, 1, 22, 18, 2800), (5, 5, 1, 25, 7, 2750), (6, 6, 1, 25, 14, 2950), (7, 7, 1, 26, 6, 2850), (8, 8, 1, 14, 16, 2400), (9, 9, 1, 18, 14, 2800), (10, 10, 1, 17, 9, 2100), (11, 11, 1, 22, 12, 2600), (12, 12, 1, 15, 10, 2700), (13, 13, 1, 14, 12, 2500), (14, 14, 1, 18, 5, 2200), (15, 15, 1, 16, 9, 2650), (16, 16, 1, 23, 5, 2450), (17, 17, 1, 35, 12, 2900), (18, 18, 1, 12, 10, 2300), (19, 19, 1, 8, 14, 1950), (20, 20, 1, 14, 8, 2400), (21, 21, 1, 16, 10, 2200), (22, 22, 1, 35, 7, 2800), (23, 23, 1, 22, 15, 2100), (24, 24, 1, 18, 12, 2850), (25, 25, 1, 9, 0, 3200), (26, 26, 1, 7, 18, 2100), (27, 27, 1, 16, 18, 2700), (28, 28, 1, 14, 10, 2400), (29, 29, 1, 7, 0, 2900), (30, 30, 1, 12, 11, 2800), (31, 31, 1, 7, 0, 2950), (32, 32, 1, 24, 13, 2750), (33, 33, 1, 15, 14, 3000), (34, 34, 1, 8, 10, 2200), (35, 35, 1, 6, 7, 2400), (36, 36, 1, 0, 0, 2300), (37, 37, 1, 10, 10, 2500), (38, 38, 1, 12, 0, 2600), (39, 39, 1, 0, 0, 1800), (40, 40, 1, 0, 0, 1500), (41, 41, 1, 0, 0, 1200), (42, 42, 1, 0, 0, 3100), (43, 43, 1, 0, 0, 2800), (44, 44, 1, 0, 0, 2900), (45, 45, 1, 0, 0, 3000), (46, 46, 1, 0, 12, 2600), (47, 47, 1, 5, 7, 2500), (48, 48, 1, 0, 0, 2200), (49, 49, 1, 6, 8, 2600), (50, 50, 1, 0, 0, 2400), (51, 51, 1, 0, 0, 2700), (52, 52, 1, 0, 0, 1900), (53, 53, 1, 0, 0, 2100), (54, 54, 1, 5, 0, 2800)
    ]
    cursor.executemany("INSERT INTO estadisticas (id, jugador_id, partido_id, goles, asistencias, minutos_jugados) VALUES (?, ?, ?, ?, ?, ?)", stats)

    conn.commit()
    conn.close()
    print("Database restored to original schema and populated successfully!")

if __name__ == "__main__":
    restore_and_populate()
