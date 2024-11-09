from sqlalchemy import delete, insert, select
from sqlalchemy.orm import Session
from app import models

def create_citanje_knjige(db: Session, knjiga_id: int, clan_id: int):
    knjiga_exists = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()
    if knjiga_exists is None:
        return {"error": "Knjiga not found"}
    
    clan_exists = db.execute(select(models.ClanPorodice).where(models.ClanPorodice.id == clan_id)).scalar_one_or_none()
    if clan_exists is None:
        return {"error": "Clan not found"}
    
    citanje_exists = db.execute(select(models.citanje_knjige).where(models.citanje_knjige.c.clan_id == clan_id, models.citanje_knjige.c.knjiga_id == knjiga_id)).first()
    if citanje_exists:
        return {"error": "Record already exists"}
    
    db.execute(insert(models.citanje_knjige).values(clan_id=clan_id, knjiga_id=knjiga_id))
    db.commit()

    return {"message": "Citanje knjige succesfully created"}

def delete_citanje_knjige(db: Session, knjiga_id: int, clan_id: int):
    citanje_exists = db.execute(select(models.citanje_knjige).where(models.citanje_knjige.c.clan_id == clan_id, models.citanje_knjige.c.knjiga_id == knjiga_id)).first()
    if citanje_exists is None:
        return {"error": "Record not found"}
    
    db.execute(
        delete(models.citanje_knjige).where(
            models.citanje_knjige.c.clan_id == clan_id,
            models.citanje_knjige.c.knjiga_id == knjiga_id
        )
    )
    db.commit()

    return {"message" : "Citanje knjige succesfully deleted"}