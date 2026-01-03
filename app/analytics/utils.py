from sqlalchemy.orm import Session
from app.expenses.models import Expense
from datetime import datetime
from collections import defaultdict

def get_monthly_summary(db: Session, user_id: int):
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    summary = defaultdict(list)

    for exp in expenses:
        month = exp.expense_date.strftime("%Y-%m")
        summary[month].append(exp.amount)

    result = []
    for month, amounts in summary.items():
        result.append({
            "month": month,
            "total_amount": sum(amounts),
            "average_amount": sum(amounts)/len(amounts),
            "highest_amount": max(amounts)
        })
    return result

def get_category_summary(db: Session, user_id: int):
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    categories = defaultdict(float)
    for exp in expenses:
        categories[exp.category] += exp.amount
    return dict(categories)
