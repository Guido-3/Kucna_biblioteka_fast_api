from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

def create_clan(db: Session, clan: schemas.ClanCreate):
    zanr_exists = db.execute(select(models.Zanr).where(models.Zanr.id == clan.omiljeni_zanr_id)).scalar_one_or_none()
    if clan.omiljeni_zanr_id and zanr_exists is None:
        return None
    
    db_clan = models.ClanPorodice(
        ime = clan.ime,
        omiljeni_zanr_id = clan.omiljeni_zanr_id
    )

    db.add(db_clan)
    db.commit()
    db.refresh(db_clan)

    return db_clan

def get_clan(db: Session, clan_id: int):
    result = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()

    return result

def get_clanovi(db: Session, skip: int = 0, limit: int = None):
    query = select(models.ClanPorodice).offset(skip)

    if query is not None:
        query = query.limit(limit)

    result = db.execute(query)

    return result.scalars().all()

def get_omiljeni_zanr_clana(db:Session, clan_id: int):
    clan = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()
    
    if clan:
        return clan.omiljeni_zanr
    
    return None

def get_knjige_koje_je_procitao_clan(db:Session, clan_id: int):
    clan = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()
    
    if clan:
        return clan.knjige
    
    return None

def update_clan(db: Session, clan_id: int, clan: schemas.ClanUpdate):
    db_clan = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()

    if db_clan is None:
        return None
    
    db_clan.ime = clan.ime
    zanr_exists = db.execute(select(models.Zanr).where(models.Zanr.id == clan.omiljeni_zanr_id)).scalar_one_or_none()
    if clan.omiljeni_zanr_id and zanr_exists is None:
        return None
    
    db_clan.omiljeni_zanr_id = clan.omiljeni_zanr_id

    db.commit()
    db.refresh(db_clan)

    return db_clan

def delete_clan(db: Session, clan_id: int):
    db_clan = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()

    if db_clan is None:
        return None
    
    db.delete(db_clan)
    db.commit()

    return db_clan