from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import knjiga_zanr_crud
from app.database import get_db

router = APIRouter()

@router.post("/knjiga_zanr/")
def create_knjiga_zanr(data: schemas.KnjigaZanrCreate,db: Session = Depends(get_db)):
    result  = knjiga_zanr_crud.create_knjiga_zanr(db=db, knjiga_id=data.knjiga_id, zanr_id=data.zanr_id)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@router.delete("/knjiga_zanr/")
def delete_knjiga_zanr(data: schemas.KnjigaZanrCreate, db: Session = Depends(get_db)):
    result = knjiga_zanr_crud.delete_knjiga_zanr(db=db, knjiga_id=data.knjiga_id, zanr_id=data.zanr_id)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

