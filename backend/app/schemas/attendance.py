from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    clock_in: Optional[time]
    clock_out: Optional[time]
    working_hours: Optional[float]
    status: Optional[str] = "present"

class LeaveRequestCreate(BaseModel):
    employee_id: int
    leave_type: str
    from_date: date
    to_date: date
    reason: Optional[str]
    status: Optional[str] = "pending"
    approver_id: Optional[int]

class LeaveRequestUpdate(BaseModel):
    status: str
    approver_id: Optional[int]
