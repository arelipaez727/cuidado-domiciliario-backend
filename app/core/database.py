from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from app.core.config import settings

# Configuración específica para SQLite en entornos multihilo como FastAPI
connect_args = (
    {"check_same_thread": False}
    if settings.DATABASE_URL.startswith("sqlite")
    else {}
)

# 1. El Engine: Es el punto central de conexión con la Base de Datos
engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    echo=settings.DEBUG  # Si DEBUG=True, imprime las consultas SQL reales en la consola
)

# 2. SessionLocal: Fabrica de sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 3. Base: Clase padre de la cual heredarán todos los Modelos ORM (tablas)
Base = declarative_base()


# 4. Generador de Sesiones (Inyección de Dependencias)
def get_db() -> Generator[Session, None, None]:
    """
    Crea una nueva sesión de base de datos para cada petición HTTP.
    Utiliza el patrón 'yield' para asegurar que la sesión se cierre
    después de responder al cliente, evitando fugas de conexiones.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()