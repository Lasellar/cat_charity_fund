from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.sql import func


class BaseModel:
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=func.now)
    close_date = Column(DateTime)
