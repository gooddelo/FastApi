'''import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database
'''
from sqlalchemy.orm import Session
import models, schemas
import database

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_client(db: Session, user_id: int):
    return db.query(models.Client).filter(models.Client.id == user_id).first()

def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, user: schemas.ClientCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Client(
            email=user.email, hashed_password=fake_hashed_password, number = user.number, advetisment_souce_id = user.advetisment_souce_id
            )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_identification(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Identification).offset(skip).limit(limit).all()


#---------------------------------------------------------------------------------------------------------

def create_client_identification(db: Session, item: schemas.IdentificationCreate, user_id: int):
    db_item = models.Identification(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_client_notes(db: Session, item: schemas.NotesCreate, user_id: int):
    db_item = models.Notes(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_client_contraidications(db: Session, item: schemas.ContraidicationsCreate, user_id: int):
    db_item = models.Contraidications(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_client_source(db: Session, item: schemas.SourceCreate, user_id: int):
    db_item = models.Source(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_client_telegram(db: Session, item: schemas.TelegramCreate, user_id: int):
    db_item = models.Telegram(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

'''def create_client_Phone_number(db: Session, item: schemas.Phone_numberCreate, user_id: int):
    db_item = models.Phone_number(**item.dict(), client_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item'''




