from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings
from app.core.database import get_db
from app.main import app
from app.models import Base


def test_person_crud(tmp_path) -> None:
    db_path = tmp_path / "person_api.db"
    test_engine = create_engine(
        f"sqlite:///{db_path}",
        connect_args={"check_same_thread": False},
    )
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

    Base.metadata.create_all(bind=test_engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    try:
        prefix = get_settings().api_prefix

        create_resp = client.post(
            f"{prefix}/persons",
            json={
                "name": "Alice",
                "display_name": "Alice Zhang",
                "aliases": ["Ali"],
                "tags": ["core"],
                "privacy_level": "family",
            },
        )
        assert create_resp.status_code == 201
        created = create_resp.json()
        person_id = created["id"]
        assert created["name"] == "Alice"
        assert created["aliases"] == ["Ali"]

        list_resp = client.get(f"{prefix}/persons")
        assert list_resp.status_code == 200
        listed = list_resp.json()
        assert len(listed) == 1
        assert listed[0]["id"] == person_id

        get_resp = client.get(f"{prefix}/persons/{person_id}")
        assert get_resp.status_code == 200
        assert get_resp.json()["display_name"] == "Alice Zhang"

        update_resp = client.patch(
            f"{prefix}/persons/{person_id}",
            json={"bio": "Family member", "aliases": ["Ali", "A"]},
        )
        assert update_resp.status_code == 200
        updated = update_resp.json()
        assert updated["bio"] == "Family member"
        assert updated["aliases"] == ["Ali", "A"]

        delete_resp = client.delete(f"{prefix}/persons/{person_id}")
        assert delete_resp.status_code == 204

        missing_resp = client.get(f"{prefix}/persons/{person_id}")
        assert missing_resp.status_code == 404
    finally:
        app.dependency_overrides.clear()
        Base.metadata.drop_all(bind=test_engine)
