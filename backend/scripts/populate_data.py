import sqlite3
import os

def populate():
    db_path = os.path.join(os.path.dirname(__file__), "..", "app.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Clear existing data
    cursor.execute("DELETE FROM estadisticas")
    cursor.execute("DELETE FROM jugadores")
    cursor.execute("DELETE FROM partidos")
    cursor.execute("DELETE FROM equipos")

    # 1. Inserción de Equipos (Teams)
    equipos = [
        (1, 'Real Madrid', 'Santiago Bernabéu'),
        (2, 'Manchester City', 'Etihad Stadium'),
        (3, 'Bayern Munich', 'Allianz Arena'),
        (4, 'Paris Saint-Germain', 'Parc des Princes'),
        (5, 'FC Barcelona', 'Camp Nou'),
        (6, 'Inter Milan', 'San Siro'),
        (7, 'Liverpool FC', 'Anfield'),
        (8, 'Arsenal FC', 'Emirates Stadium'),
        (9, 'River Plate', 'Estadio Monumental'),
        (10, 'AC Milan', 'San Siro'),
        (11, 'Borussia Dortmund', 'Signal Iduna Park'),
        (12, 'Juventus', 'Allianz Stadium'),
        (13, 'Atletico Madrid', 'Metropolitano'),
        (14, 'Bayer Leverkusen', 'BayArena'),
        (15, 'Aston Villa', 'Villa Park'),
        (16, 'Napoli', 'Diego Armando Maradona'),
        (17, 'Chelsea FC', 'Stamford Bridge'),
        (18, 'Benfica', 'Estádio da Luz'),
        (19, 'Sporting CP', 'José Alvalade'),
        (20, 'AS Roma', 'Stadio Olimpico')
    ]
    cursor.executemany("INSERT INTO equipos (id, nombre, estadio) VALUES (?, ?, ?)", equipos)

    # 2. Inserción de Jugadores (Players)
    # Using 'nombre_completo' based on PRAGMA check
    jugadores = [
        # Real Madrid
        (1, 1, 'Vinícius Júnior', 'Delantero'), (2, 1, 'Jude Bellingham', 'Mediocampista'), (3, 1, 'Kylian Mbappé', 'Delantero'), (4, 1, 'Luka Modrić', 'Mediocampista'), (5, 1, 'Thibaut Courtois', 'Arquero'),
        # Manchester City
        (6, 2, 'Erling Haaland', 'Delantero'), (7, 2, 'Kevin De Bruyne', 'Mediocampista'), (8, 2, 'Phil Foden', 'Mediocampista'), (9, 2, 'Rodri', 'Mediocampista'), (10, 2, 'Ederson', 'Arquero'),
        # Bayern Munich
        (11, 3, 'Harry Kane', 'Delantero'), (12, 3, 'Jamal Musiala', 'Mediocampista'), (13, 3, 'Leroy Sané', 'Delantero'), (14, 3, 'Joshua Kimmich', 'Mediocampista'), (15, 3, 'Manuel Neuer', 'Arquero'),
        # PSG
        (16, 4, 'Ousmane Dembélé', 'Delantero'), (17, 4, 'Achraf Hakimi', 'Defensor'), (18, 4, 'Gianluigi Donnarumma', 'Arquero'), (19, 4, 'Warren Zaïre-Emery', 'Mediocampista'), (20, 4, 'Marquinhos', 'Defensor'),
        # FC Barcelona
        (21, 5, 'Robert Lewandowski', 'Delantero'), (22, 5, 'Lamine Yamal', 'Delantero'), (23, 5, 'Pedri', 'Mediocampista'), (24, 5, 'Ronald Araújo', 'Defensor'), (25, 5, 'Marc-André ter Stegen', 'Arquero'),
        # Inter Milan
        (26, 6, 'Lautaro Martínez', 'Delantero'), (27, 6, 'Nicolò Barella', 'Mediocampista'), (28, 6, 'Alessandro Bastoni', 'Defensor'), (29, 6, 'Hakan Çalhanoğlu', 'Mediocampista'), (30, 6, 'Yann Sommer', 'Arquero'),
        # Liverpool
        (31, 7, 'Mohamed Salah', 'Delantero'), (32, 7, 'Virgil van Dijk', 'Defensor'), (33, 7, 'Alexis Mac Allister', 'Mediocampista'), (34, 7, 'Trent Alexander-Arnold', 'Defensor'), (35, 7, 'Alisson Becker', 'Arquero'),
        # Arsenal
        (36, 8, 'Bukayo Saka', 'Delantero'), (37, 8, 'Martin Ødegaard', 'Mediocampista'), (38, 8, 'William Saliba', 'Defensor'), (39, 8, 'Declan Rice', 'Mediocampista'), (40, 8, 'David Raya', 'Arquero'),
        # River Plate
        (41, 9, 'Miguel Borja', 'Delantero'), (42, 9, 'Franco Armani', 'Arquero'), (43, 9, 'Paulo Díaz', 'Defensor'), (44, 9, 'Claudio Echeverri', 'Mediocampista'), (45, 9, 'Rodrigo Aliendro', 'Mediocampista'),
        # AC Milan
        (46, 10, 'Rafael Leão', 'Delantero'), (47, 10, 'Theo Hernández', 'Defensor'), (48, 10, 'Christian Pulisic', 'Delantero'), (49, 10, 'Fikayo Tomori', 'Defensor'), (50, 10, 'Mike Maignan', 'Arquero')
    ]
    cursor.executemany("INSERT INTO jugadores (id, equipo_id, nombre_completo, posicion) VALUES (?, ?, ?, ?)", jugadores)

    # 3. Inserción de Partidos (Matches)
    partidos = [
        (1, 1, 5, '2025-10-15', 3, 1),
        (2, 2, 4, '2026-05-02', 3, 1),
        (3, 1, 7, '2026-05-05', 2, 2),
        (4, 17, 16, '2026-05-08', 2, 2),
        (5, 5, 20, '2026-05-10', 3, 0),
        (6, 3, 18, '2026-05-12', 2, 1),
        (7, 9, 6, '2026-05-15', 1, 2),
        (8, 11, 15, '2026-05-18', 2, 0),
        (9, 19, 8, '2026-05-20', 1, 1),
        (10, 14, 10, '2026-05-23', 3, 1),
        (11, 13, 12, '2026-05-26', 2, 0)
    ]
    cursor.executemany("INSERT INTO partidos (id, equipo_local_id, equipo_visitante_id, fecha, goles_local, goles_visitante) VALUES (?, ?, ?, ?, ?, ?)", partidos)

    # 4. Inserción de Estadísticas (Player_Stats)
    # Using columns based on PRAGMA check: id, jugador_id, partido_id, goles, asistencias, minutos_jugados
    estadisticas = [
        (1, 1, 1, 1, 1, 90), (2, 2, 1, 1, 0, 90), (3, 3, 1, 1, 0, 85), (4, 22, 1, 1, 0, 75), (5, 23, 1, 0, 1, 90), (6, 5, 1, 0, 0, 90), (7, 25, 1, 0, 0, 90),
        (100, 2, 2, 1, 0, 90), (101, 4, 2, 1, 1, 85), (102, 24, 2, 1, 1, 90), (103, 5, 2, 1, 0, 90), (104, 8, 2, 0, 1, 80),
        (105, 1, 3, 2, 0, 90), (106, 26, 3, 0, 2, 90), (107, 9, 3, 1, 1, 90), (108, 30, 3, 1, 0, 85), (109, 31, 3, 0, 1, 90),
        (110, 23, 4, 1, 1, 90), (111, 22, 4, 2, 0, 90),
        (112, 6, 5, 2, 1, 90), (113, 20, 5, 1, 0, 75), (114, 35, 5, 0, 1, 85), (115, 33, 5, 0, 0, 90),
        (116, 3, 6, 2, 0, 90), (117, 28, 6, 0, 1, 80), (118, 27, 6, 1, 0, 90),
        (119, 13, 7, 1, 0, 90), (120, 7, 7, 2, 0, 90), (121, 38, 7, 0, 1, 90),
        (122, 21, 8, 1, 0, 80), (123, 15, 8, 1, 1, 90), (124, 19, 8, 0, 0, 90),
        (125, 32, 9, 1, 0, 90), (126, 12, 9, 1, 0, 90),
        (127, 18, 10, 1, 2, 90), (128, 14, 10, 1, 0, 90),
        (129, 17, 11, 2, 0, 90), (130, 16, 11, 0, 0, 90)
    ]
    cursor.executemany("INSERT INTO estadisticas (id, jugador_id, partido_id, goles, asistencias, minutos_jugados) VALUES (?, ?, ?, ?, ?, ?)", estadisticas)

    conn.commit()
    conn.close()
    print("Database populated successfully!")

if __name__ == "__main__":
    populate()
