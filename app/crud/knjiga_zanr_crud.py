from sqlalchemy.orm import Session 
from sqlalchemy import delete, select, insert
from app import models


def create_knjiga_zanr(db: Session, knjiga_id: int, zanr_id: int):
    knjiga_exists = db.execute(select(models.Knjiga).where(models.Knjiga.id == knjiga_id)).scalar_one_or_none()

    if knjiga_exists is None:
        return {"error": "Knjiga does not exists"}
    
    zanr_exists = db.execute(select(models.Zanr).where(models.Zanr.id == zanr_id)).scalar_one_or_none()

    if zanr_exists is None:
        return {"error": "Zanr does not exists"}
    
    knjiga_zanr_exists = db.execute(select(models.knjiga_zanr).where(models.knjiga_zanr.c.knjiga_id == knjiga_id, models.knjiga_zanr.c.zanr_id == zanr_id)).first()
    if knjiga_zanr_exists:
        return {"error" : "Record already exists"}
    
    db.execute(insert(models.knjiga_zanr).values(knjiga_id=knjiga_id, zanr_id=zanr_id))
    db.commit()

    return {"message": "knjiga_zanr succesfully created"}

def delete_knjiga_zanr(db: Session, knjiga_id: int, zanr_id: int):
    knjiga_zanr_exists = db.execute(select(models.knjiga_zanr).where(models.knjiga_zanr.c.knjiga_id == knjiga_id, models.knjiga_zanr.c.zanr_id == zanr_id)).first()

    if knjiga_zanr_exists is None:
        return {"error": "Record not found"}
    
    db.execute(
        delete(models.knjiga_zanr).where(
            models.knjiga_zanr.c.knjiga_id == knjiga_id,
            models.knjiga_zanr.c.zanr_id == zanr_id
        )
    )
    db.commit()

    return {"message": "knjiga_zanr succesfully deleted"}

