from fastapi import FastAPI

app = FastAPI(
    title="ExpenseGuard AI",
    description="Behavior-aware personal finance intelligence backend",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "ExpenseGuard AI running"}
