from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str
    app_description: str
    database_url: str
    secret: str = 'SECRET'
    jwt_lifetime_seconds: int

    class Config:
        env_file = '.env'


settings = Settings()
