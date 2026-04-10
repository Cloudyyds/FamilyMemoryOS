from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class PersonBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)
    display_name: Optional[str] = Field(default=None, max_length=128)
    aliases: list[str] = Field(default_factory=list)
    birth_date: Optional[date] = None
    death_date: Optional[date] = None
    bio: Optional[str] = None
    tags: list[str] = Field(default_factory=list)
    privacy_level: str = Field(default="family", max_length=32)


class PersonCreate(PersonBase):
    pass


class PersonUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=128)
    display_name: Optional[str] = Field(default=None, max_length=128)
    aliases: Optional[list[str]] = None
    birth_date: Optional[date] = None
    death_date: Optional[date] = None
    bio: Optional[str] = None
    tags: Optional[list[str]] = None
    privacy_level: Optional[str] = Field(default=None, max_length=32)


class PersonRead(PersonBase):
    id: int
    created_at: datetime
    updated_at: datetime
