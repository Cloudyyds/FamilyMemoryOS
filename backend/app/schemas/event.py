from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    event_type: str = Field(..., min_length=1, max_length=64)
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = None
    event_type: Optional[str] = Field(default=None, min_length=1, max_length=64)
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class EventRead(EventBase):
    id: int
    created_at: datetime
    updated_at: datetime
