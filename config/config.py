from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Указываем настройки, где получаем значения переменных окружений """
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DB_URL: str = f"postgresql+asyncpg://"

    class Config:
        env_file = ".env"


settings = Settings()

DATABASE_URL = settings.DB_URL + (f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
                                  f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_NAME}")
