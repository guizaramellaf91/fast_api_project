from fastapi import APIRouter, Depends, HTTPException
from api.models.client import Client
from typing import List
from api.dependencies.authorizer import auth_access
from .interface import list_clients

router = APIRouter()

@router.get("/clients", response_model=List[Client])
async def get_clients(current_user: str = Depends(auth_access)):
    if current_user:
        return list_clients
    else:
        raise HTTPException(status_code=401, detail="Não autorizado")