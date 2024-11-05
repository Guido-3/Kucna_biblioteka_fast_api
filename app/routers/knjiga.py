from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import knjiga_crud
from app.database import get_db

router = APIRouter()

@router.post("/knjige/", response_model=schemas.Knjiga)
def create_knjiga(knjiga: schemas.KnjigaCreate, db: Session = Depends(get_db)):
    return knjiga_crud.create_knjiga(db=db, knjiga = knjiga)

@router.get("/knjige/{knjiga_id}", response_model=schemas.Knjiga)
def get_knjiga(knjiga_id: int, db: Session = Depends(get_db)):
    knjiga = knjiga_crud.get_knjiga(db=db, knjiga_id=knjiga_id)

    if knjiga is None:
        raise HTTPException(status_code=404, detail="Knjiga not found")
    
    return knjiga

@router.get("/knjige/", response_model=list[schemas.Knjiga])
def get_knjige(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    return knjiga_crud.get_knjige(db=db, skip=skip, limit=limit)

@router.get("/knjige/{knjiga_id}/zanrovi", response_model=list[schemas.Zanr])
def get_zanrovi_knjige(knjiga_id: int, db: Session = Depends(get_db)):
    knjiga = knjiga_crud.get_knjiga(db=db, knjiga_id=knjiga_id)

    if knjiga is None:
        raise HTTPException(status_code=404, detail="knjiga not found")
    
    return knjiga_crud.get_zanrovi_knjige(db=db, knjiga_id=knjiga_id)

@router.get("/knjige/{knjiga_id}/clanovi", response_model=list[schemas.Clan])
def get_clanovi_koji_su_procitali_knjigu(knjiga_id: int, db: Session = Depends(get_db)):
    return knjiga_crud.get_clanovi_koji_su_procitali_knjigu(db=db, knjiga_id=knjiga_id)

@router.get("/knjige/{knjiga_id}/autor", response_model=schemas.Autor)
def get_autora_knjige(knjiga_id: int, db: Session = Depends(get_db)):
    knjiga = knjiga_crud.get_knjiga(db=db, knjiga_id=knjiga_id)

    if knjiga is None:
        raise HTTPException(status_code=404, detail="knjiga not found")
    
    return knjiga_crud.get_autora_knjige(db=db, knjiga_id=knjiga_id)

@router.put("/knjige/{knjiga_id}", response_model=schemas.Knjiga)
def update_knjiga(knjiga_id: int, knjiga: schemas.Knjiga, db: Session = Depends(get_db)):
    updated_knjiga = knjiga_crud.update_knjiga(db=db, knjiga_id=knjiga_id, knjiga=knjiga)

    if updated_knjiga is None:
        raise HTTPException(status_code=404, detail="knjiga not found")
    
    return updated_knjiga

@router.delete("/knjige/{knjiga_id}", response_model=schemas.Knjiga)
def delete_knjiga(knjiga_id: int, db: Session = Depends(get_db)):
    deleted_knjiga = knjiga_crud.delete_knjiga(db=db, knjiga_id=knjiga_id)

    if deleted_knjiga is None:
        raise HTTPException(status_code=404, detail="knjiga not found")
    
    return deleted_knjiga
