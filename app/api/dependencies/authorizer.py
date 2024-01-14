from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.jwt_utils import decode_token, SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def auth_access(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Não autorizado")
        return username
    except Exception as e:
        raise HTTPException(status_code=401, detail="Não autorizado")
