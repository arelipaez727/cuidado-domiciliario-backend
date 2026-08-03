from passlib.context import CryptContext

# Configuración del contexto de hashing indicando bcrypt como esquema principal
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def obtener_password_hash(password: str) -> str:
    """Recibe una contraseña en texto plano y devuelve su hash seguro bcrypt."""
    return pwd_context.hash(password)


def verificar_password(password_plana: str, password_hashed: str) -> bool:
    """Verifica si una contraseña en texto plano coincide con el hash guardado."""
    return pwd_context.verify(password_plana, password_hashed)