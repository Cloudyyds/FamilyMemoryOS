from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RelationshipBase(BaseModel):
    from_person_id: int
    to_person_id: int
    relation_type: str = Field(..., min_length=1, max_length=64)
    note: Optional[str] = None
    confidence: Optional[float] = None


class RelationshipCreate(RelationshipBase):
    pass


class RelationshipUpdate(BaseModel):
    relation_type: Optional[str] = Field(default=None, min_length=1, max_length=64)
    note: Optional[str] = None
    confidence: Optional[float] = None


class RelationshipRead(RelationshipBase):
    id: int
    created_at: datetime
    updated_at: datetime
