from pydantic import BaseModel
from datetime import date

class EventsBase(BaseModel):
    id : int
    title : str
    describe : str
    classroom : str
    date_event : date
    phone_number : str
