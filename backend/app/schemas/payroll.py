from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SalaryCreate(BaseModel):
    employee_id: int
    basic_salary: float
    allowances: Optional[float] = 0.0
    deductions: Optional[float] = 0.0
    net_salary: float

class PayslipResponse(BaseModel):
    id: int
    employee_id: int
    salary_id: int
    month: str
    generated_at: datetime
    pdf_path: Optional[str]
    class Config:
        orm_mode = True
