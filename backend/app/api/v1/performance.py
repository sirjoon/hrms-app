from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.performance import ReviewCreate, GoalCreate
from app.core.security import get_current_user, require_role
from app.core.database import SessionLocal
from app.models.performance import PerformanceReview, Goal
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter(prefix="/performance", tags=["performance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/review", dependencies=[Depends(require_role(["Manager", "Admin"]))])
async def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    db_review = PerformanceReview(**review.dict(), created_at=datetime.utcnow())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.post("/goal", dependencies=[Depends(require_role(["Employee", "Manager"]))])
async def set_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    db_goal = Goal(**goal.dict(), created_at=datetime.utcnow())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal
