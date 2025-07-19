from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.core.security import get_current_user, require_role
from app.core.database import SessionLocal
from app.models.employee import Employee
from sqlalchemy.orm import Session

router = APIRouter(prefix="/employees", tags=["employees"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EmployeeResponse, dependencies=[Depends(require_role(["Admin", "HR"]))])
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(employee_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse, dependencies=[Depends(require_role(["Admin", "HR"]))])
async def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/{employee_id}", dependencies=[Depends(require_role(["Admin"]))])
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"detail": "Employee deleted"}

@router.get("/", response_model=list[EmployeeResponse], dependencies=[Depends(require_role(["Admin", "HR", "Manager"]))])
async def list_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

# Document upload endpoint placeholder
@router.post("/{employee_id}/documents", dependencies=[Depends(require_role(["Admin", "HR", "Employee"]))])
async def upload_document(employee_id: int, file, db: Session = Depends(get_db)):
    # Implement file upload logic here
    return {"detail": "Document uploaded"}
