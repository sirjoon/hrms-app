from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ReviewCreate(BaseModel):
    employee_id: int
    reviewer_id: int
    review_date: date
    comments: Optional[str]
    rating: int

class GoalCreate(BaseModel):
    employee_id: int
    description: str
    due_date: Optional[date]
    status: Optional[str] = "pending"
