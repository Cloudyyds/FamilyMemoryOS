from app.models import Artifact, Event, MemorySegment, Person, Relationship
from app.models.base import Base
from app.schemas import (
    ArtifactCreate,
    EventCreate,
    MemorySegmentCreate,
    PersonCreate,
    RelationshipCreate,
)


def test_model_tables_registered() -> None:
    assert Person.__tablename__ == "persons"
    assert Relationship.__tablename__ == "relationships"
    assert Event.__tablename__ == "events"
    assert Artifact.__tablename__ == "artifacts"
    assert MemorySegment.__tablename__ == "memory_segments"

    expected_tables = {
        "persons",
        "relationships",
        "events",
        "artifacts",
        "memory_segments",
    }
    assert expected_tables.issubset(set(Base.metadata.tables.keys()))


def test_schema_instantiation() -> None:
    person = PersonCreate(name="Alice")
    relation = RelationshipCreate(from_person_id=1, to_person_id=2, relation_type="parent")
    event = EventCreate(title="Family Dinner", event_type="gathering")
    artifact = ArtifactCreate(
        artifact_type="text",
        title="Diary",
        file_path="data/diary.txt",
        source_kind="manual",
    )
    segment = MemorySegmentCreate(artifact_id=1, content="A memory fragment")

    assert person.name == "Alice"
    assert relation.relation_type == "parent"
    assert event.title == "Family Dinner"
    assert artifact.artifact_type == "text"
    assert segment.evidence_level == "B"
