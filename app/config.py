from pydantic import BaseSettings


class Settings(BaseSettings):
    lru_size = int = 100000
    ttl = int = 864000
    class Config:
        env_file = ".env"

settings = Settings()