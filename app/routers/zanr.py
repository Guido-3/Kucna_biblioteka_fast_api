from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import zanr_crud
from app.database import get_db

router = APIRouter()

@router.post("/zanrovi/", response_model=schemas.Zanr)
def create_zanr(zanr: schemas.Zanr, db: Session = Depends(get_db)):
    return zanr_crud.create_zanr(db=db, zanr=zanr)

@router.get("/zanrovi/{zanr_id}", response_model=schemas.Zanr)
def get_zanr(zanr_id: int, db: Session = Depends(get_db)):
    zanr  = zanr_crud.get_zanr(db=db, zanr_id=zanr_id)

    if zanr is None:
        raise HTTPException(status_code=404, detail="Zanr not found")
    
    return zanr

@router.get("zanrovi/", response_model=list[schemas.Zanr])
def get_zanrovi(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    return zanr_crud.get_zanrovi(db-db, skip=skip, limit=limit)

@router.get("/zanrovi/{zanr_id}/knjige", response_model=list[schemas.Knjiga])
def get_knjige_ovog_zanra(zanr_id: int, db: Session = Depends(get_db)):
    zanr  = zanr_crud.get_zanr(db=db, zanr_id=zanr_id)

    if zanr is None:
        raise HTTPException(status_code=404, detail="Zanr not found")
    
    return zanr_crud.get_knjige_ovog_zanra(db=db, zanr_id=zanr_id)

@router.get("/zanrovi/{zanr_id}/clanovi", response_model=list[schemas.Clan])
def get_clanovi_kojima_je_ovo_omiljeni_zanr(zanr_id: int, db: Session = Depends(get_db)):
    zanr  = zanr_crud.get_zanr(db=db, zanr_id=zanr_id)

    if zanr is None:
        raise HTTPException(status_code=404, detail="Zanr not found")
    
    return zanr_crud.get_clanove_kojima_je_ovo__omiljeni_zanr(db-db, zanr_id=zanr_id)

@router.put("/zanrovi/{zanr_id}", response_model=schemas.Zanr)
def update_zanr(zanr_id: int, zanr: schemas.Zanr, db: Session = Depends(get_db)):
    updated_zanr = zanr_crud.update_zanr(db-db, zanr_id=zanr_id, zanr=zanr)

    if updated_zanr is None:
        raise HTTPException(status_code=404, detail="Zanr not found")
    
    return updated_zanr

@router.delete("/zanrovi/{zanr_id}", response_model=schemas.Zanr)
def delete_zanr(zanr_id: int, db: Session = Depends(get_db)):
    deleted_zanr = zanr_crud.delete_zanr(db-db, zanr_id=zanr_id)

    if deleted_zanr is None:
        raise HTTPException(status_code=404, detail="Zanr not found")
    
    return deleted_zanr