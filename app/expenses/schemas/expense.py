from pydantic import BaseModel
from datetime import date
from typing import Optional


class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    expense_date: date


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        from_attributes = True
