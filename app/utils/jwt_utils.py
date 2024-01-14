import jwt
from datetime import datetime, timedelta
from decouple import config

SECRET_KEY = config("JWT_SECRET_KEY")
ALGORITHM = config("ALGORITHM")

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        return None
    except Exception as e:
        print(f"Erro ao decodificar token: {e}")
        return None

def create_access_token(data: dict, expires_delta: timedelta):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        print(f"Erro ao criar token: {e}")
        return None
