from datetime import timedelta, datetime
from jose import jwt

SECRET_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def create_acess_token(data: dict):
    _data = data.copy()
    expired = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    _data.update({'exp': expired})

    token_jwt = jwt.encode(_data, SECRET_KEY, algorithm= ALGORITHM)
    return token_jwt

def verify_acess_token(token: str):
    change = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return change.get('sub')