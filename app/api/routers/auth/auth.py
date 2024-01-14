from datetime import timedelta
from fastapi import HTTPException
from fastapi import APIRouter
from api.models.user import User
from utils.jwt_utils import create_access_token
from decouple import config

router = APIRouter()

@router.post("/auth")
async def authenticate_user(user: User):
    if user.username == "admin" and user.password == "admin":
        access_token_expires = timedelta(
        seconds=int(config('JWT_ACCESS_TOKEN_EXPIRES')))
        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "Bearer"}
    else:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")