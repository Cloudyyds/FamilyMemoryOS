from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ArtifactBase(BaseModel):
    artifact_type: str = Field(..., min_length=1, max_length=64)
    title: str = Field(..., min_length=1, max_length=255)
    file_path: str = Field(..., min_length=1, max_length=1024)
    original_filename: Optional[str] = Field(default=None, max_length=255)
    source_kind: str = Field(..., min_length=1, max_length=64)
    owner_person_id: Optional[int] = None
    created_time: Optional[datetime] = None
    privacy_level: str = Field(default="family", max_length=32)


class ArtifactCreate(ArtifactBase):
    pass


class ArtifactUpdate(BaseModel):
    artifact_type: Optional[str] = Field(default=None, min_length=1, max_length=64)
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    file_path: Optional[str] = Field(default=None, min_length=1, max_length=1024)
    original_filename: Optional[str] = Field(default=None, max_length=255)
    source_kind: Optional[str] = Field(default=None, min_length=1, max_length=64)
    owner_person_id: Optional[int] = None
    created_time: Optional[datetime] = None
    privacy_level: Optional[str] = Field(default=None, max_length=32)


class ArtifactRead(ArtifactBase):
    id: int
    imported_time: datetime
