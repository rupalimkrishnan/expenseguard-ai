from pydantic import BaseModel
from typing import Dict

class MonthlySummary(BaseModel):
    month: str
    total_amount: float
    average_amount: float
    highest_amount: float

class CategorySummary(BaseModel):
    category_totals: Dict[str, float]
