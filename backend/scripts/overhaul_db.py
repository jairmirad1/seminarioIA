import sqlite3
import os
import re

def create_new_schema():
    db_path = os.path.join(os.path.dirname(__file__), "..", "app.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing tables if they exist
    cursor.execute("DROP TABLE IF EXISTS estadisticas")
    cursor.execute("DROP TABLE IF EXISTS partidos")
    cursor.execute("DROP TABLE IF EXISTS jugadores")
    cursor.execute("DROP TABLE IF EXISTS equipos")

    # Create new tables
    cursor.execute("""
    CREATE TABLE jugadores (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        club_actual TEXT NOT NULL,
        posicion_categoria TEXT NOT NULL,
        rol_posicion TEXT,
        goles_promedio REAL DEFAULT 0,
        asistencias_promedio REAL DEFAULT 0,
        precision_pases REAL DEFAULT 0,
        metricas_destacadas TEXT
    )
    """)
    
    # Data parsing and insertion
    # Delanteros
    delanteros = [
        (1, "Erling Haaland", "Manchester City", "Delantero", "Goleador", 40, 8, 0, "~40 Goles | ~8 Asistencias"),
        (2, "Kylian Mbappé", "Real Madrid", "Delantero", "Extremo/Goleador", 35, 10, 0, "~35 Goles | ~10 Asistencias"),
        (3, "Harry Kane", "Bayern Múnich", "Delantero", "Goleador", 38, 12, 0, "~38 Goles | ~12 Asistencias"),
        (4, "Vinícius Júnior", "Real Madrid", "Delantero", "Extremo", 22, 18, 0, "~22 Goles | ~18 Asistencias"),
        (5, "Robert Lewandowski", "FC Barcelona", "Delantero", "Goleador", 25, 7, 0, "~25 Goles | ~7 Asistencias"),
        (6, "Mohamed Salah", "Liverpool", "Delantero", "Extremo", 25, 14, 0, "~25 Goles | ~14 Asistencias"),
        (7, "Lautaro Martínez", "Inter de Milán", "Delantero", "Goleador", 26, 6, 0, "~26 Goles | ~6 Asistencias"),
        (8, "Lamine Yamal", "FC Barcelona", "Delantero", "Extremo", 14, 16, 0, "~14 Goles | ~16 Asistencias"),
        (9, "Bukayo Saka", "Arsenal", "Delantero", "Extremo", 18, 14, 0, "~18 Goles | ~14 Asistencias"),
        (10, "Rodrygo Goes", "Real Madrid", "Delantero", "Extremo", 17, 9, 0, "~17 Goles | ~9 Asistencias"),
        (11, "Phil Foden", "Manchester City", "Delantero", "Extremo/MP", 22, 12, 0, "~22 Goles | ~12 Asistencias"),
        (12, "Heung-min Son", "Tottenham", "Delantero", "Extremo", 15, 10, 0, "~15 Goles | ~10 Asistencias"),
        (13, "Rafael Leão", "AC Milan", "Delantero", "Extremo", 14, 12, 0, "~14 Goles | ~12 Asistencias"),
        (14, "Victor Osimhen", "Galatasaray", "Delantero", "Goleador", 18, 5, 0, "~18 Goles | ~5 Asistencias"),
        (15, "Antoine Griezmann", "Atlético de Madrid", "Delantero", "MP/Goleador", 16, 9, 0, "~16 Goles | ~9 Asistencias"),
        (16, "Alexander Isak", "Newcastle", "Delantero", "Goleador", 23, 5, 0, "~23 Goles | ~5 Asistencias"),
        (17, "Viktor Gyökeres", "Sporting CP", "Delantero", "Goleador", 35, 12, 0, "~35 Goles | ~12 Asistencias"),
        (18, "Khvicha Kvaratskhelia", "Napoli", "Delantero", "Extremo", 12, 10, 0, "~12 Goles | ~10 Asistencias"),
        (19, "Ousmane Dembélé", "PSG", "Delantero", "Extremo", 8, 14, 0, "~8 Goles | ~14 Asistencias"),
        (20, "Luis Díaz", "Liverpool", "Delantero", "Extremo", 14, 8, 0, "~14 Goles | ~8 Asistencias"),
        (21, "Julián Álvarez", "Atlético de Madrid", "Delantero", "Goleador", 16, 10, 0, "~16 Goles | ~10 Asistencias"),
        (22, "Cristiano Ronaldo", "Al-Nassr", "Delantero", "Goleador", 35, 7, 0, "~35 Goles | ~7 Asistencias"),
        (23, "Lionel Messi", "Inter Miami", "Delantero", "MP/Extremo", 22, 15, 0, "~22 Goles | ~15 Asistencias"),
    ]

    # Mediocampistas
    mediocampistas = [
        (24, "Jude Bellingham", "Real Madrid", "Mediocampista", "Volante Ofensivo", 18, 12, 0, "~18 Goles | ~12 Asistencias"),
        (25, "Rodri Hernández", "Manchester City", "Mediocampista", "Pivote / MCD", 9, 0, 92, "~9 Goles | 92% Efectividad de pases"),
        (26, "Kevin De Bruyne", "Manchester City", "Mediocampista", "Organizador", 7, 18, 0, "~7 Goles | ~18 Asistencias"),
        (27, "Florian Wirtz", "Bayer Leverkusen", "Mediocampista", "Mediapunta", 16, 18, 0, "~16 Goles | ~18 Asistencias"),
        (28, "Jamal Musiala", "Bayern Múnich", "Mediocampista", "Mediapunta", 14, 10, 0, "~14 Goles | ~10 Asistencias"),
        (29, "Federico Valverde", "Real Madrid", "Mediocampista", "Box-to-Box", 7, 0, 0, "~7 Goles | 11.5 km Recorridos por partido"),
        (30, "Martin Ødegaard", "Arsenal", "Mediocampista", "Organizador", 12, 11, 0, "~12 Goles | ~11 Asistencias"),
        (31, "Declan Rice", "Arsenal", "Mediocampista", "Pivote / Mixto", 7, 0, 0, "~7 Goles | ~2.5 Intercepciones por partido"),
        (32, "Cole Palmer", "Chelsea", "Mediocampista", "Volante / Extremo", 24, 13, 0, "~24 Goles | ~13 Asistencias"),
        (33, "Bruno Fernandes", "Manchester United", "Mediocampista", "Mediapunta", 15, 14, 0, "~15 Goles | ~14 Asistencias"),
        (34, "Ilkay Gündogan", "Manchester City", "Mediocampista", "Organizador", 8, 10, 0, "~8 Goles | ~10 Asistencias"),
        (35, "Alexis Mac Allister", "Liverpool", "Mediocampista", "Volante Mixto", 6, 7, 0, "~6 Goles | ~7 Asistencias"),
        (36, "Aurélien Tchouaméni", "Real Madrid", "Mediocampista", "Pivote defensivo", 0, 0, 0, "~2.8 Duelos aéreos ganados por partido"),
        (37, "Bernardo Silva", "Manchester City", "Mediocampista", "Interior / Extremo", 10, 10, 0, "~10 Goles | ~10 Asistencias"),
        (38, "Hakan Çalhanoglu", "Inter de Milán", "Mediocampista", "Regidor de juego", 12, 0, 0, "~12 Goles (especialista en penales/tiros libres)"),
        (39, "Pedri González", "FC Barcelona", "Mediocampista", "Organizador", 0, 0, 90, "90% Efectividad en campo rival"),
        (40, "Gavi (Páez)", "FC Barcelona", "Mediocampista", "Volante Mixto", 0, 0, 0, "~4.5 Entradas ganadas por partido"),
        (41, "Luka Modric", "Real Madrid", "Mediocampista", "Organizador", 0, 0, 89, "89% Precisión de pases (entrando de recambio)"),
    ]

    # Defensores
    defensores = [
        (42, "Virgil van Dijk", "Liverpool", "Defensor", "Central", 0, 0, 0, "~72% Duelos aéreos ganados"),
        (43, "Antonio Rüdiger", "Real Madrid", "Defensor", "Central", 0, 0, 0, "~65% Duelos defensivos ganados"),
        (44, "William Saliba", "Arsenal", "Defensor", "Central", 0, 0, 91, "~91% Precisión de pases en salida"),
        (45, "Rúben Dias", "Manchester City", "Defensor", "Central", 0, 0, 0, "~0.4 Errores que llevan a disparo por temporada"),
        (46, "Trent Alexander-Arnold", "Liverpool", "Defensor", "Lateral Derecho", 0, 12, 0, "~12 Asistencias por temporada"),
        (47, "Achraf Hakimi", "PSG", "Defensor", "Lateral Derecho", 5, 7, 0, "~5 Goles | ~7 Asistencias por temporada"),
        (48, "Alfonso Davies", "Bayern Múnich", "Defensor", "Lateral Izquierdo", 0, 0, 0, "Velocidad punta de 36.5 km/h"),
        (49, "Theo Hernández", "AC Milan", "Defensor", "Lateral Izquierdo", 6, 8, 0, "~6 Goles | ~8 Asistencias por temporada"),
        (50, "Kyle Walker", "Manchester City", "Defensor", "Lateral Derecho", 0, 0, 0, "Especialista en duelos 1v1 defensivos"),
        (51, "Alessandro Bastoni", "Inter de Milán", "Defensor", "Central", 0, 0, 0, "~5 Pases largos completados por partido"),
        (52, "John Stones", "Manchester City", "Defensor", "Central / Pivote", 0, 0, 94, "~94% Eficiencia de pase bajo presión"),
        (53, "Ronald Araújo", "FC Barcelona", "Defensor", "Central", 0, 0, 0, "~70% Duelos terrestres ganados"),
        (54, "Gabriel Magalhães", "Arsenal", "Defensor", "Central", 5, 0, 0, "~5 Goles de pelota parada por temporada"),
    ]

    all_players = delanteros + mediocampistas + defensores
    cursor.executemany("""
    INSERT INTO jugadores (id, nombre, club_actual, posicion_categoria, rol_posicion, goles_promedio, asistencias_promedio, precision_pases, metricas_destacadas)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, all_players)

    conn.commit()
    conn.close()
    print("Database overhauled and populated with new stats successfully!")

if __name__ == "__main__":
    create_new_schema()
