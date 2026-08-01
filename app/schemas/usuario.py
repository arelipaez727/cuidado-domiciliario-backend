from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from app.schemas.rol import RolResponse


# 1. Atributos comunes
class UsuarioBase(BaseModel):
    email: EmailStr


# 2. Esquema para CREAR un usuario (Lo que ENTRA por la API)
class UsuarioCreate(UsuarioBase):
    password: str
    rol_id: int


# 3. Esquema para DEVOLVER un usuario (Lo que SALE por la API)
class UsuarioResponse(UsuarioBase):
    id: int
    activo: bool
    rol_id: int
    rol: RolResponse
    creado_en: datetime

    model_config = ConfigDict(from_attributes=True)