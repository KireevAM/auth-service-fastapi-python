from fastapi import FastAPI
from app.api.v1.endpoints import auth
from app.core.config import settings
from app.db.database import engine
from app.db import models

# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Auth Service is running!"}