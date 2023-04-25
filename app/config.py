from pydantic import BaseSettings


class Settings(BaseSettings):
    lrusize: int
    ttl: int
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    db_user: str
    db_password: str
    db_host: str
    db_minpool: int
    db_maxpool: int    
    class Config:
        env_file = ".env"

settings = Settings()