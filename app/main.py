from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import services, models, schemas
from database import SessionLocal, engine

services.create_database()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.Client)
def create_client(user: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_user = services.get_client_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_client(db=db, user=user)


@app.get("/users/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_clients(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.Client)
def read_client(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_client(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/idntify/", response_model=schemas.Identification)
def create_item_for_client(
    user_id: int, item: schemas.IdentificationCreate, db: Session = Depends(get_db)
):
    return services.create_client_identification(db=db, item=item, user_id=user_id)

@app.post("/users/{user_id}/notes/", response_model=schemas.Notes)
def create_notes_for_client(
    user_id: int, item: schemas.NotesCreate, db: Session = Depends(get_db)
):
    return services.create_client_notes(db=db, item=item, user_id=user_id)

@app.post("/users/{user_id}/contraidications/", response_model=schemas.Contraidications)
def create_contraidications_for_client(
    user_id: int, item: schemas.ContraidicationsCreate, db: Session = Depends(get_db)
):
    return services.create_client_contraidications(db=db, item=item, user_id=user_id)

@app.post("/users/{user_id}/source/", response_model=schemas.Source)
def create_source_for_client(
    user_id: int, item: schemas.SourceCreate, db: Session = Depends(get_db)
):
    return services.create_client_source(db=db, item=item, user_id=user_id)

@app.post("/users/{user_id}/telegram/", response_model=schemas.Telegram)
def create_telegram_for_client(
    user_id: int, item: schemas.TelegramCreate, db: Session = Depends(get_db)
):
    return services.create_client_telegram(db=db, item=item, user_id=user_id)

'''@app.post("/users/{user_id}/phone/", response_model=schemas.Phone_number)
def create_Phone_number_for_client(
    user_id: int, item: schemas.Phone_numberCreate, db: Session = Depends(get_db)
):
    return services.create_client_Phone_number(db=db, item=item, user_id=user_id)'''