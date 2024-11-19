"""Defines the pydantic-settings config."""

from pathlib import Path

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Settings for the notes app.

    Instantiating this class loads the settings from environment variables. If
    environment variables for a particular setting are not found, the default values
    specified in this class are used.
    """

    markdown_files_dir: DirectoryPath = Path("pages")
    port: int = 10_000  # 10,000 is the default port for Render.
    hostname: str = "0.0.0.0"  # noqa: S104, because I don't understand the warning...
    auto_reload: bool = False
    pages_path: DirectoryPath = Path("./pages/")
    client_path: DirectoryPath = Path("./client/dist/")

    model_config = SettingsConfigDict(env_prefix="notes_")


parsed_config = Config()
