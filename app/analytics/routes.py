from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.dependencies import get_current_user
from app.analytics.utils import (
    get_monthly_summary,
    get_category_summary
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/monthly")
def monthly_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_monthly_summary(db, current_user.id)


@router.get("/category")
def category_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_category_summary(db, current_user.id)
