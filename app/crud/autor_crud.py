from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

def create_autor(db: Session, autor: schemas.AutorCreate):
    db_autor = models.Autor(
        ime = autor.ime
    )

    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)

    return db_autor

def get_autor(db: Session, autor_id: int):
    result = db.execute(select(models.Autor).where(models.Autor.id == autor_id))

    return result.scalar_one_or_none()

def get_autori(db: Session, skip: int = 0, limit: int = None):
    query = select(models.Autor).offset(skip)
    if query is not None:
        query = query.limit(limit)
    
    result = db.execute(query)

    return result.scalars().all()

def get_knjige_autora(db: Session, autor_id: int):
    autor = db.execute(select(models.Autor).where(models.Autor.id == autor_id)).scalar_one_or_none()
    if autor:
        return autor.knjige
    
    return None
    

def update_autor(db: Session, autor_id: int, autor: schemas.AutorUpdate):
    db_autor = db.execute(select(models.Autor).where(models.Autor.id == autor_id)).scalar_one_or_none()

    if db_autor is None:
        return None

    db_autor.ime = autor.ime

    db.commit()
    db.refresh(db_autor)
    
    return db_autor

def delete_autor(db: Session, autor_id: int):
    db_autor = db.execute(select(models.Autor).where(models.Autor.id == autor_id)).scalar_one_or_none()

    if db_autor is None:
        return None
    
    db.delete(db_autor)
    db.commit()

    return db_autor