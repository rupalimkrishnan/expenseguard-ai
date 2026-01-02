from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base
from app.database import models
from app.auth.routes import router as auth_router

app = FastAPI(
    title="ExpenseGuard AI",
    description="Behavior-aware personal finance intelligence backend",
    version="0.1.0"
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "ExpenseGuard AI running"}
