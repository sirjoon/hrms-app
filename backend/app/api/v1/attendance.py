from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.attendance import AttendanceCreate, LeaveRequestCreate, LeaveRequestUpdate
from app.core.security import get_current_user, require_role
from app.core.database import SessionLocal
from app.models.attendance import Attendance, LeaveRequest, Holiday
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

router = APIRouter(prefix="/attendance", tags=["attendance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clock-in", dependencies=[Depends(require_role(["Employee"]))])
async def clock_in(attendance: AttendanceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    att = Attendance(
        employee_id=current_user["id"],
        date=attendance.date,
        clock_in=attendance.clock_in or datetime.now().time(),
        status=attendance.status or "present"
    )
    db.add(att)
    db.commit()
    db.refresh(att)
    return att

@router.post("/clock-out", dependencies=[Depends(require_role(["Employee"]))])
async def clock_out(attendance: AttendanceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    att = db.query(Attendance).filter(
        Attendance.employee_id == current_user["id"],
        Attendance.date == attendance.date
    ).first()
    if not att:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    att.clock_out = attendance.clock_out or datetime.now().time()
    # Calculate working hours if clock_in and clock_out are present
    if att.clock_in and att.clock_out:
        att.working_hours = (
            datetime.combine(datetime.today(), att.clock_out) - datetime.combine(datetime.today(), att.clock_in)
        ).seconds / 3600.0
    db.commit()
    db.refresh(att)
    return att

@router.get("/logs")
async def get_attendance_logs(date_from: str, date_to: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    logs = db.query(Attendance).filter(
        Attendance.employee_id == current_user["id"],
        Attendance.date >= date_from,
        Attendance.date <= date_to
    ).all()
    return logs

@router.post("/leave", dependencies=[Depends(require_role(["Employee"]))])
async def submit_leave_request(leave: LeaveRequestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    req = LeaveRequest(
        employee_id=current_user["id"],
        leave_type=leave.leave_type,
        from_date=leave.from_date,
        to_date=leave.to_date,
        reason=leave.reason,
        status="pending",
        approver_id=leave.approver_id
    )
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

@router.put("/leave/{leave_id}", dependencies=[Depends(require_role(["Manager", "Admin"]))])
async def update_leave_request(leave_id: int, leave: LeaveRequestUpdate, db: Session = Depends(get_db)):
    req = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if not req:
        raise HTTPException(status_code=404, detail="Leave request not found")
    req.status = leave.status
    req.approver_id = leave.approver_id
    db.commit()
    db.refresh(req)
    return req

@router.get("/holidays")
async def list_holidays(db: Session = Depends(get_db)):
    holidays = db.query(Holiday).all()
    return holidays
