from app.core.config import clear_settings_cache, get_settings


def test_settings_loaded_from_env_file(tmp_path, monkeypatch) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "FAMILY_MEMORY_APP_NAME=FamilyMemoryOS Test API",
                "FAMILY_MEMORY_ENV=test",
                "FAMILY_MEMORY_DEBUG=true",
                "FAMILY_MEMORY_API_PREFIX=/api/v1",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.delenv("FAMILY_MEMORY_APP_NAME", raising=False)
    monkeypatch.delenv("FAMILY_MEMORY_ENV", raising=False)
    monkeypatch.delenv("FAMILY_MEMORY_DEBUG", raising=False)
    monkeypatch.delenv("FAMILY_MEMORY_API_PREFIX", raising=False)

    clear_settings_cache()
    settings = get_settings(env_file=env_file)

    assert settings.app_name == "FamilyMemoryOS Test API"
    assert settings.app_env == "test"
    assert settings.app_debug is True
    assert settings.api_prefix == "/api/v1"

    clear_settings_cache()


def test_os_env_overrides_env_file(tmp_path, monkeypatch) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "FAMILY_MEMORY_APP_NAME=FromEnvFile",
                "FAMILY_MEMORY_ENV=local",
                "FAMILY_MEMORY_DEBUG=false",
                "FAMILY_MEMORY_API_PREFIX=/file",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setenv("FAMILY_MEMORY_APP_NAME", "FromOS")
    monkeypatch.setenv("FAMILY_MEMORY_ENV", "dev")
    monkeypatch.setenv("FAMILY_MEMORY_DEBUG", "true")
    monkeypatch.setenv("FAMILY_MEMORY_API_PREFIX", "/os")

    clear_settings_cache()
    settings = get_settings(env_file=env_file)

    assert settings.app_name == "FromOS"
    assert settings.app_env == "dev"
    assert settings.app_debug is True
    assert settings.api_prefix == "/os"

    clear_settings_cache()
