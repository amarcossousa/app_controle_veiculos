from pydantic import BaseModel, EmailStr
from typing import Optional

class Users(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class UsersSimple(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    email: EmailStr
    password: str


class LoginSucess(BaseModel):
    user: UsersSimple
    acess_token: str

class ControleKmSchema(BaseModel):
    id: Optional[int] = None
    data: str
    destino: str
    hora_saida: str
    hora_chegada: str
    km_inicial: int
    km_final: int
    objetivo: str
    qt_combustivel: int