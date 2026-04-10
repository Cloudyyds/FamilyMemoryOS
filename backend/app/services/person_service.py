from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.person import Person
from app.repositories import person_repository
from app.schemas.person import PersonCreate, PersonRead, PersonUpdate


def _person_to_read(person: Person) -> PersonRead:
    aliases = person.aliases if isinstance(person.aliases, list) else []
    tags = person.tags if isinstance(person.tags, list) else []

    return PersonRead(
        id=person.id,
        name=person.name,
        display_name=person.display_name,
        aliases=aliases,
        birth_date=person.birth_date,
        death_date=person.death_date,
        bio=person.bio,
        tags=tags,
        privacy_level=person.privacy_level,
        created_at=person.created_at,
        updated_at=person.updated_at,
    )


def create_person(db: Session, payload: PersonCreate) -> PersonRead:
    person = person_repository.create_person(db, payload)
    return _person_to_read(person)


def get_person_or_404(db: Session, person_id: int) -> Person:
    person = person_repository.get_person(db, person_id)
    if person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Person {person_id} not found"
        )
    return person


def get_person(db: Session, person_id: int) -> PersonRead:
    person = get_person_or_404(db, person_id)
    return _person_to_read(person)


def list_persons(db: Session, offset: int = 0, limit: int = 50) -> list[PersonRead]:
    persons = person_repository.list_persons(db, offset=offset, limit=limit)
    return [_person_to_read(person) for person in persons]


def _person_update_to_dict(payload: PersonUpdate) -> dict:
    if hasattr(payload, "model_dump"):
        return payload.model_dump(exclude_unset=True)
    return payload.dict(exclude_unset=True)


def update_person(db: Session, person_id: int, payload: PersonUpdate) -> PersonRead:
    person = get_person_or_404(db, person_id)
    updates = _person_update_to_dict(payload)
    if updates:
        payload_for_repo = PersonUpdate(**updates)
        person = person_repository.update_person(db, person, payload_for_repo)
    return _person_to_read(person)


def delete_person(db: Session, person_id: int) -> None:
    person = get_person_or_404(db, person_id)
    person_repository.delete_person(db, person)
