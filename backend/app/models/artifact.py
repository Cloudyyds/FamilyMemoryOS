from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.models.base import Base


class Artifact(Base):
    __tablename__ = "artifacts"

    id = Column(Integer, primary_key=True, index=True)
    artifact_type = Column(String(64), nullable=False)
    title = Column(String(255), nullable=False)
    file_path = Column(String(1024), nullable=False)
    original_filename = Column(String(255), nullable=True)
    source_kind = Column(String(64), nullable=False)
    owner_person_id = Column(ForeignKey("persons.id"), nullable=True)
    created_time = Column(DateTime(timezone=True), nullable=True)
    imported_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    privacy_level = Column(String(32), nullable=False, default="family")
