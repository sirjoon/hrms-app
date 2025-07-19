from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import LoginRequest, Token
from app.core.security import create_access_token, verify_password, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
async def login(form_data: LoginRequest):
    # Authenticate user and return JWT
    pass

@router.get("/me")
async def get_user(current_user=Depends(get_current_user)):
    return current_user
