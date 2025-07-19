from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Salary(Base):
    __tablename__ = "salaries"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    basic_salary = Column(Float, nullable=False)
    allowances = Column(Float, default=0.0)
    deductions = Column(Float, default=0.0)
    net_salary = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    employee = relationship("Employee")

class Payslip(Base):
    __tablename__ = "payslips"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    salary_id = Column(Integer, ForeignKey("salaries.id"))
    month = Column(String, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)
    pdf_path = Column(String)
    employee = relationship("Employee")
    salary = relationship("Salary")
