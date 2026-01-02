from fastapi import FastAPI
from app.database.database import engine
from app.database.base import Base
from app.database import models

app = FastAPI(
    title="ExpenseGuard AI",
    description="Behavior-aware personal finance intelligence backend",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ExpenseGuard AI running"}
