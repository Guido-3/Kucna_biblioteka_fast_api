from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import clan_crud
from app.database import get_db

router = APIRouter()

@router.post("/clanovi/", response_model=schemas.Clan)
def create_clan(clan: schemas.Clan, db: Session = Depends(get_db)):
    return clan_crud.create_clan(db=db, clan=clan)

@router.get("/clanovi/{clan_id}", response_model=schemas.Clan)
def get_clan(clan_id: int, db: Session = Depends(get_db)):
    clan = clan_crud.get_clan(db=db, clan_id=clan_id)
    if clan is None:
        raise HTTPException(status_code=404, detail="Clan not found")

    return clan

@router.get("/clanovi/", response_class=list[schemas.Clan])
def get_clanovi(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    return clan_crud.get_clanovi(db=db, skip=skip, limit=limit)

@router.get("/clanovi/{clan_id}/omiljeni_zanr", response_model=schemas.Zanr)
def get_omiljeni_zanr_clana(clan_id: int, db: Session = Depends(get_db)):
    clan = clan_crud.get_clan(db=db, clan_id=clan_id)
    
    if clan is None:
        raise HTTPException(status_code=404, detail="Clan not found")
    
    return clan_crud.get_omiljeni_zanr_clana(db=db, clan_id=clan_id)

@router.get("/clanovi/{clan_id}/knjige", response_model=list[schemas.Knjiga])
def get_knjige_koje_je_procitao_clan(clan_id: int, db: Session = Depends(get_db)):
    clan = clan_crud.get_clan(db=db, clan_id=clan_id)
    
    if clan is None:
        raise HTTPException(status_code=404, detail="Clan not found")
    
    return clan_crud.get_knjige_koje_je_procitao_clan(db=db, clan_id=clan_id)

@router.put("/clanovi/{clan_id}", response_model=schemas.Clan)
def update_clan(clan_id: int, clan: schemas.Clan, db: Session = Depends(get_db)):
    updated_clan = clan_crud.update_clan(db=db, clan_id=clan_id, clan=clan)

    if updated_clan is None:
        raise HTTPException(status_code=404, detail="Clan not found")
    
    return updated_clan

@router.delete("/clanovi/{clan_id}", response_model=schemas.Clan)
def delete_clan(clan_id: int, db: Session = Depends(get_db)):
    deleted_clan = clan_crud.delete_clan(db=db, clan_id=clan_id)

    if deleted_clan is None:
        raise HTTPException(status_code=404, detail="Clan not found")
    
    return deleted_clan