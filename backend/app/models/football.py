from sqlalchemy import String, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Equipo(Base):
    __tablename__ = "equipos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)

    jugadores: Mapped[list["Jugador"]] = relationship("Jugador", back_populates="equipo")


class Jugador(Base):
    __tablename__ = "jugadores"

    id: Mapped[int] = mapped_column(primary_key=True)
    equipo_id: Mapped[int] = mapped_column(ForeignKey("equipos.id"), nullable=False)
    nombre_completo: Mapped[str] = mapped_column(String(100), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    posicion: Mapped[str] = mapped_column(String(50), nullable=True)
    valor_mercado_millones: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)

    equipo: Mapped["Equipo"] = relationship("Equipo", back_populates="jugadores")
    estadisticas: Mapped["Estadistica"] = relationship("Estadistica", back_populates="jugador", uselist=False)


class Estadistica(Base):
    __tablename__ = "estadisticas"

    jugador_id: Mapped[int] = mapped_column(ForeignKey("jugadores.id"), primary_key=True)
    alineaciones: Mapped[int] = mapped_column(Integer, default=0)
    goles: Mapped[int] = mapped_column(Integer, default=0)
    asistencias: Mapped[int] = mapped_column(Integer, default=0)
    tarjetas_amarillas: Mapped[int] = mapped_column(Integer, default=0)
    tarjetas_rojas: Mapped[int] = mapped_column(Integer, default=0)

    jugador: Mapped["Jugador"] = relationship("Jugador", back_populates="estadisticas")
