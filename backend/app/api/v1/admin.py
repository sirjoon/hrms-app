from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_user, require_role
from app.core.database import SessionLocal
from app.models.employee import Employee
from app.models.attendance import Attendance, LeaveRequest
from app.models.payroll import Salary
from sqlalchemy.orm import Session

router = APIRouter(prefix="/admin", tags=["admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/analytics", dependencies=[Depends(require_role(["Admin"]))])
async def get_analytics(db: Session = Depends(get_db)):
    total_employees = db.query(Employee).count()
    total_attendance = db.query(Attendance).count()
    total_leave_requests = db.query(LeaveRequest).count()
    total_salaries = db.query(Salary).count()
    return {
        "total_employees": total_employees,
        "total_attendance": total_attendance,
        "total_leave_requests": total_leave_requests,
        "total_salaries": total_salaries,
    }

@router.post("/settings", dependencies=[Depends(require_role(["Admin"]))])
async def update_settings(settings: dict):
    # Implement settings update logic here
    return {"detail": "Settings updated"}
