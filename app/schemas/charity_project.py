from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class CharityProjectBase(BaseModel):
    """Базовая схема."""
    name: str | None = Field(min_length=1, max_length=100)
    description: str | None = Field(min_length=1)
    full_amount: int | None = Field(gt=0)


class CharityProjectCreate(CharityProjectBase):
    """Схема для создания сбора."""
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    full_amount: int = Field(gt=0)


class CharityProjectUpdate(CharityProjectBase):
    """Схема для обновления сбора."""
    @field_validator('name')
    def validate_name(cls, value):
        if value is None:
            raise ValueError('Название проекта не может быть пустым.')
        return value


class CharityProjectDB(CharityProjectBase):
    """Схема для возврата из БД."""
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime | None = None

    class Config:
        from_attributes = True
