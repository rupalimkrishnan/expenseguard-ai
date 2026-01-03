from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.auth.dependencies import get_current_user
from app.expenses.models import Expense
from app.expenses.schemas import ExpenseCreate

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

# Batch POST endpoint: create multiple expenses at once
@router.post("/", response_model=List[ExpenseCreate])
def create_expenses(
    expenses: List[ExpenseCreate],
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if not expenses:
        raise HTTPException(status_code=400, detail="No expenses provided")
    
    created_expenses = []
    for exp_data in expenses:
        exp = Expense(
            title=exp_data.title,
            amount=exp_data.amount,
            category=exp_data.category,
            expense_date=exp_data.expense_date,
            user_id=current_user.id
        )
        db.add(exp)
        created_expenses.append(exp)
    
    db.commit()
    return created_expenses
