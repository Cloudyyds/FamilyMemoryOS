from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, func

from app.models.base import Base


class Relationship(Base):
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True, index=True)
    from_person_id = Column(ForeignKey("persons.id"), nullable=False, index=True)
    to_person_id = Column(ForeignKey("persons.id"), nullable=False, index=True)
    relation_type = Column(String(64), nullable=False)
    note = Column(Text, nullable=True)
    confidence = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )
