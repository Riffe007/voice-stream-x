# app/config.py
# This file contains configuration settings for the FastAPI application

import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Define your configuration variables here
    # Example: API keys, database URLs, etc.
    API_KEY: str
    DATABASE_URL: str = "sqlite:///./test.db"
    ELEVEN_LABS_API_KEY: str
    OPENAI_API_KEY: str
    WHISPER_API_URL: str = "https://whisper-api.openai.com"
    ELEVEN_LABS_API_URL: str = "https://api.elevenlabs.io/v1/text-to-speech"

    class Config:
        # Loads the .env file that's in the same directory as this file
        # Requires python-dotenv package
        env_file = ".env"

# Instantiate the Settings class to load the configurations
settings = Settings()

# You can now import 'settings' from this module and access the configuration variables
# Example: settings.API_KEY
