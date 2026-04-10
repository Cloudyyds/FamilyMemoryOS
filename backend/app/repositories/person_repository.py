from sqlalchemy.orm import Session

from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate


def create_person(db: Session, payload: PersonCreate) -> Person:
    person = Person(
        name=payload.name,
        display_name=payload.display_name,
        aliases=payload.aliases,
        birth_date=payload.birth_date,
        death_date=payload.death_date,
        bio=payload.bio,
        tags=payload.tags,
        privacy_level=payload.privacy_level,
    )
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


def get_person(db: Session, person_id: int) -> Person | None:
    return db.query(Person).filter(Person.id == person_id).first()


def list_persons(db: Session, offset: int = 0, limit: int = 50) -> list[Person]:
    return db.query(Person).order_by(Person.id.asc()).offset(offset).limit(limit).all()


def update_person(db: Session, person: Person, payload: PersonUpdate) -> Person:
    if hasattr(payload, "model_dump"):
        updates = payload.model_dump(exclude_unset=True)
    else:
        updates = payload.dict(exclude_unset=True)

    for key, value in updates.items():
        setattr(person, key, value)

    db.add(person)
    db.commit()
    db.refresh(person)
    return person


def delete_person(db: Session, person: Person) -> None:
    db.delete(person)
    db.commit()
