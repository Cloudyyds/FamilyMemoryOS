from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func

from app.models.base import Base


class MemorySegment(Base):
    __tablename__ = "memory_segments"

    id = Column(Integer, primary_key=True, index=True)
    artifact_id = Column(ForeignKey("artifacts.id"), nullable=False, index=True)
    person_id = Column(ForeignKey("persons.id"), nullable=True, index=True)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    source_type = Column(String(64), nullable=True)
    timestamp = Column(DateTime(timezone=True), nullable=True)
    evidence_level = Column(String(16), nullable=False, default="B")
    privacy_level = Column(String(32), nullable=False, default="family")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
