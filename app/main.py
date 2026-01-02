from fastapi import FastAPI
from app.database.database import engine
from app.database.base import Base
from app.database import models
from app.auth.routes import router as auth_router

# 1️⃣ Create FastAPI app first
app = FastAPI(
    title="ExpenseGuard AI",
    description="Behavior-aware personal finance intelligence backend",
    version="0.1.0"
)

# 2️⃣ Include auth router
app.include_router(auth_router)

# 3️⃣ Create tables
Base.metadata.create_all(bind=engine)

# 4️⃣ Health check
@app.get("/")
def health_check():
    return {"status": "ExpenseGuard AI running"}
