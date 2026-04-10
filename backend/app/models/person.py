from sqlalchemy import JSON, Column, Date, DateTime, Integer, String, Text, func

from app.models.base import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False, index=True)
    display_name = Column(String(128), nullable=True)
    aliases = Column(JSON, nullable=False, default=list)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    bio = Column(Text, nullable=True)
    tags = Column(JSON, nullable=False, default=list)
    privacy_level = Column(String(32), nullable=False, default="family")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )
