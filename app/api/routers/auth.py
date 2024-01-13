from fastapi import HTTPException
from fastapi import APIRouter
from api.models.user import User

router = APIRouter()

@router.post("/auth")
async def authenticate_user(user: User):
    if not user.username:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")
    return {"message": "Autenticado com sucesso"}