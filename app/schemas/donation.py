from datetime import datetime

from pydantic import BaseModel, Field


class DonationBase(BaseModel):
    comment: str | None = Field(min_length=1)
    full_amount: int = Field(gt=0)


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationBase):
    id: int
    comment: str | None
    full_amount: int
    create_date: datetime

    class Config:
        from_attributes = True


class DonationDBAdmin(DonationDB):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: datetime | None = None


