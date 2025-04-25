from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Title'
    app_description: str = 'Description'
    database_url: str = "sqlite+aiosqlite:///./cat_charity_fund.db"
    secret: str = 'SECRET'
    jwt_lifetime_seconds: int = 3600

    class Config:
        env_file = '.env'


settings = Settings()
