from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    address: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    marital_status: Optional[str]
    national_id: Optional[str]
    employment_type: Optional[str] = "full_time"
    joining_date: date
    probation_end_date: Optional[date]
    confirmation_date: Optional[date]
    work_location: Optional[str]
    status: Optional[str] = "active"
    department_id: Optional[int]
    role_id: Optional[int]
    supervisor_id: Optional[int]

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    marital_status: Optional[str]
    national_id: Optional[str]
    employment_type: Optional[str]
    probation_end_date: Optional[date]
    confirmation_date: Optional[date]
    work_location: Optional[str]
    status: Optional[str]
    department_id: Optional[int]
    role_id: Optional[int]
    supervisor_id: Optional[int]

class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    address: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    marital_status: Optional[str]
    national_id: Optional[str]
    employment_type: Optional[str]
    joining_date: date
    probation_end_date: Optional[date]
    confirmation_date: Optional[date]
    work_location: Optional[str]
    status: Optional[str]
    department_id: Optional[int]
    role_id: Optional[int]
    supervisor_id: Optional[int]
    class Config:
        orm_mode = True
