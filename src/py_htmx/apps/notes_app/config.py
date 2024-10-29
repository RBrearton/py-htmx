"""Defines the pydantic-settings config."""

from pathlib import Path

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the notes app.

    Instantiating this class loads the settings from environment variables. If
    environment variables for a particular setting are not found, the default values
    specified in this class are used.
    """

    markdown_files_dir: DirectoryPath = Path("pages")

    model_config = SettingsConfigDict(env_prefix="my_prefix_")
