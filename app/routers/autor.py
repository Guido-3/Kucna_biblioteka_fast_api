from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.crud import autor_crud
from app.database import get_db

router = APIRouter()

@router.post("/autori/", response_model=schemas.Autor)
def create_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    return autor_crud.create_autor(db=db, autor=autor)

@router.get("/autori/{autor_id}", response_model=schemas.Autor)
def get_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = autor_crud.get_autor(db=db, autor_id=autor_id)

    if autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")

    return autor

@router.get("/autori/", response_model=list[schemas.Autor])
def get_autori(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    return autor_crud.get_autori(db=db, skip=skip, limit=limit)

@router.get("/autori/{autor_id}/knjige", response_model=list[schemas.Knjiga])
def get_knjige_autora(autor_id: int, db: Session = Depends(get_db)):
    autor = autor_crud.get_autor(db=db, autor_id=autor_id)

    if autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    
    return autor_crud.get_knjige_autora(db=db, autor_id=autor_id)

@router.put("/autori/{autor_id}", response_model=schemas.Autor)
def update_autor(autor_id: int, autor: schemas.AutorUpdate, db: Session = Depends(get_db)):
    updated_autor = autor_crud.update_autor(db=db, autor_id=autor_id, autor=autor)
    
    if updated_autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    
    return updated_autor

@router.delete("/autori/{autor_id}", response_model=schemas.Autor)
def delete_autor(autor_id: int, db: Session = Depends(get_db)):
    deleted_autor = autor_crud.delete_autor(db=db, autor_id=autor_id)
    
    if deleted_autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    
    return deleted_autor   