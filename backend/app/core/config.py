import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Mapping, Optional, Union


def _as_bool(value: str, default: bool = False) -> bool:
    normalized = (value or "").strip().lower()
    if not normalized:
        return default
    return normalized in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    app_debug: bool
    api_prefix: str
    database_url: str


BACKEND_ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_ENV_FILE = BACKEND_ROOT_DIR / ".env"


def _read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", maxsplit=1)
        key = key.strip()
        value = value.strip().strip("\"'")

        if key:
            values[key] = value

    return values


def _merged_env(file_values: Mapping[str, str]) -> dict[str, str]:
    merged = dict(file_values)
    # OS environment variables have higher priority than local .env.
    merged.update(os.environ)
    return merged


def clear_settings_cache() -> None:
    get_settings.cache_clear()


@lru_cache(maxsize=1)
def get_settings(env_file: Optional[Union[str, Path]] = None) -> Settings:
    file_path = Path(env_file) if env_file else DEFAULT_ENV_FILE
    config = _merged_env(_read_env_file(file_path))

    app_env = config.get("FAMILY_MEMORY_ENV", "local").strip() or "local"

    return Settings(
        app_name=config.get("FAMILY_MEMORY_APP_NAME", "FamilyMemoryOS API"),
        app_env=app_env,
        app_debug=_as_bool(config.get("FAMILY_MEMORY_DEBUG", "false")),
        api_prefix=config.get("FAMILY_MEMORY_API_PREFIX", "").strip(),
        database_url=config.get("FAMILY_MEMORY_DATABASE_URL", "sqlite:///./familymemory.db"),
    )
