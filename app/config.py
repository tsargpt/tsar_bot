from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: list[int]

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", ".env"),
        env_file_encoding="utf-8",
    )


settings = Settings()
