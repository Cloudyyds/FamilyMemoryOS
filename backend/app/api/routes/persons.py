from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.person import PersonCreate, PersonRead, PersonUpdate
from app.services import person_service

router = APIRouter(prefix="/persons", tags=["persons"])


@router.post("", response_model=PersonRead, status_code=status.HTTP_201_CREATED)
def create_person(payload: PersonCreate, db: Session = Depends(get_db)) -> PersonRead:
    return person_service.create_person(db, payload)


@router.get("", response_model=list[PersonRead])
def list_persons(
    db: Session = Depends(get_db),
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 50,
) -> list[PersonRead]:
    return person_service.list_persons(db, offset=offset, limit=limit)


@router.get("/{person_id}", response_model=PersonRead)
def get_person(person_id: int, db: Session = Depends(get_db)) -> PersonRead:
    return person_service.get_person(db, person_id)


@router.patch("/{person_id}", response_model=PersonRead)
def update_person(person_id: int, payload: PersonUpdate, db: Session = Depends(get_db)) -> PersonRead:
    return person_service.update_person(db, person_id, payload)


@router.delete("/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int, db: Session = Depends(get_db)) -> None:
    person_service.delete_person(db, person_id)
