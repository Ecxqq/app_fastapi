from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import date

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class EventsBase(BaseModel):
    id : int
    title : str
    describe : str
    classroom : str
    date_event : date
    phone_number : str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/add_event/")
async def create_event(event: EventsBase, db: db_dependency):
    db_event = models.Events(title=event.title,describe=event.describe,classroom=event.classroom,date_event=event.date_event,phone_number=event.phone_number)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    db.commit()

@app.get("/get_event_by_id/{event_id}")
async def read_event(event_id: int, db: db_dependency):
    result = db.query(models.Events).filter(models.Events.id == event_id).all()
    if not result:
        raise HTTPException(status_code=404,detail='Event with id{event_id} is not found')
    return result

@app.get("/get_all_events/")
async def read_event(db: db_dependency):
    result = db.query(models.Events).all()
    if not result:
        raise HTTPException(status_code=404,detail='Events is not found')
    return result

@app.get("/get_event_by_title/{title_text}")
async def read_event(title_text: str, db: db_dependency):
    result = db.query(models.Events).filter(models.Events.title == title_text).all()
    if not result:
        raise HTTPException(status_code=404,detail=f'Events with title{title_text} not found')
    return result