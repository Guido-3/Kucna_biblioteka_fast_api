from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas


def create_zanr(db: Session, zanr: schemas.ZanrCreate):
    db_zanr = models.Zanr(
        ime = zanr.ime
    )

    db.add(db_zanr)
    db.commit()
    db.refresh(db_zanr)

    return db_zanr

def get_zanr(db: Session, zanr_id: int):
    result = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id))

    return result.scalar_one_or_none()

def get_zanrovi(db: Session, skip: int = 0, limit: int = None):
    query = select(models.Zanr).offset(skip)
    
    if query is not None:
        query = query.limit(limit)

    result = db.execute(query)

    return result.scalars().all()

def get_knjige_ovog_zanra(db:Session, zanr_id: int):
    zanr = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id)).scalar_one_or_none()
    
    if zanr:
        return zanr.knjige

    return None

def get_clanove_kojima_je_ovo__omiljeni_zanr(db:Session, zanr_id: int):
    zanr = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id)).scalar_one_or_none()
    
    if zanr:
        return zanr.clanovi_ciji_je_omiljeni_zanr

    return None

def update_zanr(db: Session, zanr_id: int, zanr: schemas.ZanrUpdate):
    db_zanr = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id)).scalar_one_or_none()

    if db_zanr is None:
        return None

    db_zanr.ime = zanr.ime

    db.commit()
    db.refresh(db_zanr)

    return db_zanr

def delete_zanr(db: Session, zanr_id: int):
    db_zanr = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id)).scalar_one_or_none()
    if db_zanr is None:
        return None
    
    db.delete(db_zanr)
    db.commit()

    return db_zanr