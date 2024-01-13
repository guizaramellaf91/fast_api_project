from fastapi import APIRouter
from api.models.client import Client
from typing import List

router = APIRouter()

fake_clients = [
    {"id": 1, "name": "Cliente 1", "email": "cliente1@example.com"},
    {"id": 2, "name": "Cliente 2", "email": "cliente2@example.com"},
]

@router.get("/clients", response_model=List[Client])
async def get_clients():
    return fake_clients