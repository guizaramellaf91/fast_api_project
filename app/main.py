from fastapi import FastAPI
import uvicorn
from api.routers.clients import router as clients_router
from api.routers.auth import router as auth_router

app = FastAPI()
app.include_router(clients_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
