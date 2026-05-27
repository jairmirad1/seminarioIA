from datetime import date
from sqlalchemy import String, ForeignKey, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Equipo(Base):
    __tablename__ = "equipos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    ciudad: Mapped[str] = mapped_column(String(100), nullable=True)
    estadio: Mapped[str] = mapped_column(String(100), nullable=True)

    jugadores: Mapped[list["Jugador"]] = relationship("Jugador", back_populates="equipo")


class Jugador(Base):
    __tablename__ = "jugadores"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    posicion: Mapped[str] = mapped_column(String(50), nullable=True)
    numero_camiseta: Mapped[int] = mapped_column(Integer, nullable=True)
    equipo_id: Mapped[int] = mapped_column(ForeignKey("equipos.id"), nullable=False)

    equipo: Mapped["Equipo"] = relationship("Equipo", back_populates="jugadores")


class Partido(Base):
    __tablename__ = "partidos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    equipo_local_id: Mapped[int] = mapped_column(ForeignKey("equipos.id"), nullable=False)
    equipo_visitante_id: Mapped[int] = mapped_column(ForeignKey("equipos.id"), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    goles_local: Mapped[int] = mapped_column(Integer, default=0)
    goles_visitante: Mapped[int] = mapped_column(Integer, default=0)


class Estadistica(Base):
    __tablename__ = "estadisticas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    partido_id: Mapped[int] = mapped_column(ForeignKey("partidos.id"), nullable=False)
    jugador_id: Mapped[int] = mapped_column(ForeignKey("jugadores.id"), nullable=False)
    goles: Mapped[int] = mapped_column(Integer, default=0)
    asistencias: Mapped[int] = mapped_column(Integer, default=0)
    tarjetas_amarillas: Mapped[int] = mapped_column(Integer, default=0)
    tarjetas_rojas: Mapped[int] = mapped_column(Integer, default=0)
    minutos_jugados: Mapped[int] = mapped_column(Integer, default=0)
