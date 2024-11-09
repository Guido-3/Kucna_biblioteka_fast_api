from pydantic import BaseModel

#################################### Scheme za Knjigu ###############################################

class KnjigaBase(BaseModel):
    naslov: str
    autor_id: int 

class KnjigaCreate(KnjigaBase):
    pass

class KnjigaUpdate(KnjigaBase):
    pass

class Knjiga(KnjigaBase):
    id: int
    class Config:
        from_attributes=True

#################################### Scheme za Autora ###############################################

class AutorBase(BaseModel):
    ime: str

class AutorCreate(AutorBase):
    pass

class AutorUpdate(AutorBase):
    pass

class Autor(AutorBase):
    id: int

    class Config:
        from_attributes=True

#################################### Scheme za Zanr #################################################

class ZanrBase(BaseModel):
    ime: str

class ZanrCreate(ZanrBase):
    pass

class ZanrUpdate(ZanrBase):
    pass

class Zanr(ZanrBase):
    id: int

    class Config:
        from_attributes=True

#################################### Scheme za Clana porodice #######################################

class ClanBase(BaseModel):
    ime: str
    omiljeni_zanr_id: int

class ClanCreate(ClanBase):
    pass

class ClanUpdate(ClanBase):
    pass

class Clan(ClanBase):
    id: int

    class Config:
        from_attributes=True

#################################### Scheme za Knjiga Zanr #######################################

class KnjigaZanrBase(BaseModel):
    knjiga_id: int
    zanr_id: int

class KnjigaZanrCreate(KnjigaZanrBase):
    pass

class KnjigaZanr(KnjigaZanrBase):
    class Config:
        from_attributes = True

#################################### Scheme za Knjiga Zanr #######################################

class CitanjeKnjigeBase(BaseModel):
    knjiga_id: int
    clan_id: int

class CitanjeKnjigeCreate(CitanjeKnjigeBase):
    pass

class CitanjeKnjige(CitanjeKnjigeBase):
    class Config:
        from_attributes = True
