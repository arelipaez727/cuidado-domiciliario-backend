from typing import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.usuario import Usuario


class UsuarioRepository:
    """
    Capa de Acceso a Datos (DAL) para la entidad Usuario.
    Contiene únicamente consultas SQL ejecutadas a través del ORM.
    """

    def obtener_por_email(self, db: Session, email: str) -> Usuario | None:
        """Busca un usuario activo por su dirección de correo electrónico."""
        stmt = select(Usuario).where(Usuario.email == email, Usuario.activo == True)
        return db.scalar(stmt)

    def obtener_por_id(self, db: Session, usuario_id: int) -> Usuario | None:
        """Busca un usuario por su ID primario."""
        stmt = select(Usuario).where(Usuario.id == usuario_id, Usuario.activo == True)
        return db.scalar(stmt)

    def obtener_todos(self, db: Session, skip: int = 0, limit: int = 100) -> Sequence[Usuario]:
        """Obtiene una lista paginada de usuarios."""
        stmt = select(Usuario).where(Usuario.activo == True).offset(skip).limit(limit)
        return db.scalars(stmt).all()

    def crear(self, db: Session, usuario: Usuario) -> Usuario:
        """Persiste un nuevo objeto Usuario en la base de datos."""
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario


# Instancia para ser utilizada por los servicios
usuario_repository = UsuarioRepository()