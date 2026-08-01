from pydantic import BaseModel, ConfigDict


class RolBase(BaseModel):
    nombre: str
    descripcion: str | None = None


class RolCreate(RolBase):
    pass


class RolResponse(RolBase):
    id: int

    model_config = ConfigDict(from_attributes=True)