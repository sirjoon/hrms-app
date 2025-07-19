from fastapi import FastAPI
from app.api.v1 import employee, attendance, payroll, performance, auth, admin

app = FastAPI(title="HRMS API", docs_url="/docs")

app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(attendance.router)
app.include_router(payroll.router)
app.include_router(performance.router)
app.include_router(admin.router)
