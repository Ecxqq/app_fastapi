from sqlalchemy import Column,Integer,String,Date
from ..database.database import Base


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    describe = Column(String, index=True)
    classroom = Column(String, index=True)
    date_event = Column(Date, index=True)
    phone_number = Column(String, index=True)