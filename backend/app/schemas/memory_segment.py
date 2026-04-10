from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MemorySegmentBase(BaseModel):
    artifact_id: int
    person_id: Optional[int] = None
    content: str = Field(..., min_length=1)
    summary: Optional[str] = None
    source_type: Optional[str] = Field(default=None, max_length=64)
    timestamp: Optional[datetime] = None
    evidence_level: str = Field(default="B", max_length=16)
    privacy_level: str = Field(default="family", max_length=32)


class MemorySegmentCreate(MemorySegmentBase):
    pass


class MemorySegmentUpdate(BaseModel):
    person_id: Optional[int] = None
    content: Optional[str] = Field(default=None, min_length=1)
    summary: Optional[str] = None
    source_type: Optional[str] = Field(default=None, max_length=64)
    timestamp: Optional[datetime] = None
    evidence_level: Optional[str] = Field(default=None, max_length=16)
    privacy_level: Optional[str] = Field(default=None, max_length=32)


class MemorySegmentRead(MemorySegmentBase):
    id: int
    created_at: datetime
