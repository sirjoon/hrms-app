from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class PerformanceReview(Base):
    __tablename__ = "performance_reviews"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    reviewer_id = Column(Integer, ForeignKey("employees.id"))
    review_date = Column(Date, nullable=False)
    comments = Column(String)
    rating = Column(Integer)  # 1-5 scale
    created_at = Column(DateTime, default=datetime.utcnow)
    employee = relationship("Employee", foreign_keys=[employee_id])
    reviewer = relationship("Employee", foreign_keys=[reviewer_id])

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    description = Column(String, nullable=False)
    due_date = Column(Date)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    employee = relationship("Employee")
