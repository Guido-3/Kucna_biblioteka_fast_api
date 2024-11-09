# SQLITE STUDIO APK ZA PROVJERU SQLITE 

from sqlalchemy import Column, Integer, String, ForeignKey, Table, MetaData 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

knjiga_zanr = Table(
    "knjiga_zanr",
    Base.metadata,
    Column("knjiga_id", Integer, ForeignKey("knjige.id"), primary_key=True),
    Column("zanr_id", Integer, ForeignKey("zanrovi.id"), primary_key=True)
)

citanje_knjige = Table(
    "citanje_knjige",
    Base.metadata, 
    Column("knjiga_id", Integer, ForeignKey("knjige.id"), primary_key=True),
    Column("clan_id", Integer, ForeignKey("clanovi.id"), primary_key=True)
)

class Knjiga(Base):
    __tablename__ = "knjige"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    naslov: Mapped[str] = mapped_column(String, index=True)
    autor_id: Mapped[int] = mapped_column(Integer, ForeignKey("autori.id"))

    autor: Mapped["Autor"] = relationship(back_populates="knjige")
    zanrovi: Mapped[list["Zanr"]] = relationship(secondary=knjiga_zanr, back_populates="knjige")
    clanovi: Mapped[list["ClanPorodice"]] = relationship(secondary=citanje_knjige, back_populates="knjige")

class Zanr(Base):
    __tablename__ = "zanrovi"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ime: Mapped[str] = mapped_column(String, index=True)

    knjige: Mapped[list["Knjiga"]] = relationship(secondary=knjiga_zanr, back_populates="zanrovi")
    clanovi_ciji_je_omiljeni_zanr: Mapped[list["ClanPorodice"]] = relationship(back_populates="omiljeni_zanr")

class Autor(Base):
    __tablename__ = "autori"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ime: Mapped[str] = mapped_column(String, index=True)
    
    knjige: Mapped[list["Knjiga"]] = relationship(back_populates="autor")


class ClanPorodice(Base):
    __tablename__ = "clanovi"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ime: Mapped[str] = mapped_column(String, index=True)
    omiljeni_zanr_id: Mapped[int]= mapped_column(Integer, ForeignKey("zanrovi.id"))

    omiljeni_zanr: Mapped["Zanr"] = relationship(back_populates="clanovi_ciji_je_omiljeni_zanr")
    knjige: Mapped[list["Knjiga"]] = relationship(secondary=citanje_knjige, back_populates="clanovi")
