from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

def create_knjiga(db: Session, knjiga: schemas.KnjigaCreate):
    db_knjiga = models.Knjiga(
        naslov = knjiga.naslov,
        autor_id = knjiga.autor_id
    )
    
    db.add(db_knjiga)
    db.commit()
    db.refresh(db_knjiga)
    
    return db_knjiga

def get_knjiga(db: Session, knjiga_id: int):
    result = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id))

    return result.scalar_one_or_none()

def get_knjige(db: Session, skip: int = 0, limit: int = None):
    query = select(models.Knjiga).offset(skip)
    
    if query is not None:
        query = query.limit(limit)
    
    result = db.execute(query)

    return result.scalars().all()

def get_zanrovi_knjige(db: Session, knjiga_id: int):
    knjiga = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    if knjiga:
        return knjiga.zanrovi
    
    return None

def get_clanovi_koji_su_procitali_knjigu(db: Session, knjiga_id: int):
    knjiga = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    if knjiga:
        return knjiga.clanovi
    
    return None

def get_autora_knjige(db: Session, knjiga_id: int):
    knjiga = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    if knjiga:
        return knjiga.autor
    
    return None


def update_knjiga(db: Session, knjiga_id: int, knjiga: schemas.KnjigaUpdate):
    db_knjiga = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    
    if db_knjiga is None:
        return None
    
    db_knjiga.naslov = knjiga.naslov
    db_knjiga.autor_id = knjiga.autor_id
    
    db.commit()
    db.refresh(db_knjiga)

    return db_knjiga
    
def delete_knjiga(db: Session, knjiga_id: int):
    db_knjiga = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    
    if db_knjiga is None:
        return None
    
    db.delete(db_knjiga)
    db.commit()

    return db_knjiga