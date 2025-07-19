from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.payroll import SalaryCreate, PayslipResponse
from app.core.security import get_current_user, require_role
from app.core.database import SessionLocal
from app.models.payroll import Salary, Payslip
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter(prefix="/payroll", tags=["payroll"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/salary", dependencies=[Depends(require_role(["Admin"]))])
async def create_salary(salary: SalaryCreate, db: Session = Depends(get_db)):
    db_salary = Salary(**salary.dict(), created_at=datetime.utcnow())
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)
    return db_salary

@router.get("/payslip/{employee_id}", response_model=PayslipResponse, dependencies=[Depends(require_role(["Admin", "Employee"]))])
async def generate_payslip(employee_id: int, month: str, db: Session = Depends(get_db)):
    salary = db.query(Salary).filter(Salary.employee_id == employee_id).first()
    if not salary:
        raise HTTPException(status_code=404, detail="Salary not found")
    payslip = Payslip(
        employee_id=employee_id,
        salary_id=salary.id,
        month=month,
        generated_at=datetime.utcnow(),
        pdf_path=None  # Implement PDF generation logic if needed
    )
    db.add(payslip)
    db.commit()
    db.refresh(payslip)
    return payslip
