import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings

ENV_PATH = os.environ.get('AIOGRAM_DEMO_ENV_PATH', '../.env')


class Settings(BaseSettings):
    DEBUG: bool = Field(env='DEBUG')

    IMAGE_DIR: Optional[str] = Field(env='IMAGE_DIR', default=None)

    TELEGRAM_BOT_TOKEN: str = Field(env='TELEGRAM_BOT_TOKEN')
    WEATHER_API_KEY: str = Field(env='WEATHER_API_KEY')

    DB_HOST: str = Field(env='DB_HOST')
    DB_PORT: int = Field(env='DB_PORT')
    DB_BASENAME: str = Field(env='DB_BASENAME')
    DB_USERNAME: str = Field(env='DB_USERNAME')
    DB_PASSWORD: str = Field(env='DB_PASSWORD')

    @property
    def dsn(self):
        return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@" \
               f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASENAME}"

    class Config:
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'
        extra = "allow"


settings = Settings()
