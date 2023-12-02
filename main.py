from fastapi import FastAPI
from .models import models
from .database import database
from .routers import routers

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.include_router(routers.router)

