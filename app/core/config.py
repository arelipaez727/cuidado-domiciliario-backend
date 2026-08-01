from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Variables con valores por defecto (opcionales en el .env)
    PROJECT_NAME: str = "Cuidado Domiciliario API"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./cuidado_domiciliario.db"
    
    # Variables obligatorias (lanzarán error al iniciar si no están en el .env)
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Configuración para indicarle a Pydantic dónde leer el archivo
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Instancia singleton para ser importada en el resto de la aplicación
settings = Settings()