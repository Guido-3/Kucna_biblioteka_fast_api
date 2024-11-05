from fastapi import FastAPI
from app.routers import knjiga, autor, zanr, clan  # Importuj sve routere
from app.database import engine, Base

# Kreiraj tabele u bazi, ukoliko već nisu kreirane
Base.metadata.create_all(bind=engine)

# Inicijalizuj FastAPI aplikaciju
app = FastAPI()

# Dodaj sve rute
app.include_router(knjiga.router)
app.include_router(autor.router)
app.include_router(zanr.router)
app.include_router(clan.router)
