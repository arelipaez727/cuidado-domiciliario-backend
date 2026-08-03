from typing import Sequence
from sqlalchemy.orm import Session
from app.core.security import obtener_password_hash
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.repositories.usuario_repository import usuario_repository


class UsuarioService:
    """
    Capa de Lógica de Negocio para Usuarios.
    Aplica reglas operativas, validaciones y orquesta repositorios.
    """

    def crear_usuario(self, db: Session, usuario_in: UsuarioCreate) -> Usuario:
        """
        Regla de Negocio: 
        1. Verificar que el email no esté registrado.
        2. Generar el hash de la contraseña.
        3. Persistir la entidad a través del repositorio.
        """
        usuario_existente = usuario_repository.obtener_por_email(db, email=usuario_in.email)
        if usuario_existente:
            raise ValueError(f"El email '{usuario_in.email}' ya se encuentra registrado.")

        # Generar hash seguro
        hashed_password = obtener_password_hash(usuario_in.password)

        # Crear entidad del modelo SQLAlchemy
        nuevo_usuario = Usuario(
            email=usuario_in.email,
            password_hash=hashed_password,
            rol_id=usuario_in.rol_id
        )

        return usuario_repository.crear(db, nuevo_usuario)

    def obtener_por_id(self, db: Session, usuario_id: int) -> Usuario | None:
        return usuario_repository.obtener_por_id(db, usuario_id)

    def listar_usuarios(self, db: Session, skip: int = 0, limit: int = 100) -> Sequence[Usuario]:
        return usuario_repository.obtener_todos(db, skip=skip, limit=limit)


# Instancia para ser reutilizada en los Routers
usuario_service = UsuarioService()