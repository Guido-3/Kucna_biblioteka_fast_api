from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
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
    id = Column(Integer, primary_key=True, index=True)
    naslov = Column(String, index=True)
    autor_id = Column(Integer, ForeignKey("autori.id"))

    autor = relationship("Autor", back_populates="knjige")
    zanrovi = relationship("Zanr", secondary=knjiga_zanr, back_populates="knjige")
    clanovi = relationship("ClanPorodice", secondary=citanje_knjige, back_populates="cita_knjigu")

class Zanr(Base):
    __tablename__ = "zanrovi"
    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, index=True)
    knjige = relationship("Knjiga", secondary=knjiga_zanr, back_populates="zanrovi")

class Autor(Base):
    __tablename__ = "autori"
    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, index=True)
    
    knjige = relationship("Knjiga", back_populates="autor")


class ClanPorodice(Base):
    __tablename__ = "clanovi"
    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, index=True)
    omiljeni_zanr_id = Column(Integer, ForeignKey("zanrovi.id"))

    omiljeni_zanr = relationship("Zanr")
    cita_knjigu = relationship("Knjiga", secondary=citanje_knjige, back_populates="clanovi")
