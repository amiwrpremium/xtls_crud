from typing import Union, List, Optional
from pathlib import Path
import secrets

from pydantic import AnyHttpUrl, BaseSettings, validator, EmailStr


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SERVER_NAME: str = "http://127.0.0.1:8000"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 5001

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = 'XTLS_CRUD'

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "amiwr"
    POSTGRES_PASSWORD: str = "0024444103"
    POSTGRES_DB: str = "inj_test"

    BACKEND_DATABASE_URL: str = f'sqlite:///{str(Path(__file__).parent)}/web.db'
    ASYNC_BACKEND_DATABASE_URL: str = BACKEND_DATABASE_URL.replace('sqlite://', 'sqlite+aiosqlite://')

    FIRST_SUPERUSER: EmailStr = "amiwrpremium@gmail.com"
    FIRST_SUPERUSER_PASSWORD: str = "0024444103"

    ADMIN_TOKEN: Optional[str] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzAzNjc4NTAsInN1YiI6IjEifQ." \
                                 "PI416k6bpJqV6NyNxg4Egjcg2I1BiAMSBIVwvd7WB1U"

    class Config:
        case_sensitive = True

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
