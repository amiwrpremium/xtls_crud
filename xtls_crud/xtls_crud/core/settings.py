import typing as t

from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    # General
    DEBUG: bool = False

    # Environment
    ENVIRONMENT: t.Literal['dev', 'prod', 'local'] = 'dev'

    # Database is in current directory with name: 'x-ui.db' (use absolute path to change)
    if ENVIRONMENT == 'dev' or ENVIRONMENT == 'local':
        _current_path = Path(__file__).parent
        DATABASE_URL: str = f'sqlite:///{_current_path}/x-ui.db'
    else:
        DATABASE_URL: str = '/etc/x-ui/x-ui.db'

    ASYNC_DB_URL: str = DATABASE_URL.replace('sqlite://', 'sqlite+aiosqlite://')


settings = Settings()
