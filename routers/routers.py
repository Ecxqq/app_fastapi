from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemes.schemes import EventsBase
from ..models.models import Events
from ..database.database import get_db

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/api/works",
    tags=["Works"]
)

@router.post("/add_event/")
async def create_event(event: EventsBase, db: db_dependency):
    db_event = Events(title=event.title,describe=event.describe,classroom=event.classroom,date_event=event.date_event,phone_number=event.phone_number)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    db.commit()

@router.get("/get_event_by_id/{event_id}")
async def read_event(event_id: int, db: db_dependency):
    result = db.query(Events).filter(Events.id == event_id).all()
    if not result:
        raise HTTPException(status_code=404,detail='Event with id{event_id} is not found')
    return result

@router.get("/get_all_events/")
async def read_event(db: db_dependency):
    result = db.query(Events).all()
    if not result:
        raise HTTPException(status_code=404,detail='Events is not found')
    return result

@router.get("/get_event_by_title/{title_text}")
async def read_event(title_text: str, db: db_dependency):
    result = db.query(Events).filter(Events.title == title_text).all()
    if not result:
        raise HTTPException(status_code=404,detail=f'Events with title{title_text} not found')
    return result