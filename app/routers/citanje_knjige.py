from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import citanje_knjige_crud
from app.database import get_db

router = APIRouter()

@router.post("/citanje_knjige/")
def create_citanje(data: schemas.CitanjeKnjigeCreate, db: Session = Depends(get_db)):
    result = citanje_knjige_crud.create_citanje_knjige(db=db, knjiga_id=data.knjiga_id, clan_id=data.clan_id)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@router.delete("/citanje_knjige/")
def delete_citanje_knjige(data: schemas.CitanjeKnjigeCreate, db: Session = Depends(get_db)):
    result = citanje_knjige_crud.delete_citanje_knjige(db=db, knjiga_id=data.knjiga_id, clan_id=data.clan_id)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    return result