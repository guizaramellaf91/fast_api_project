from fastapi import APIRouter
from .auth.auth import router as auth_router
from .clients.clients import router as clients_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(clients_router)