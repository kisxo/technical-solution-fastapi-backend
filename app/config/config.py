from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    # Appwrite
    APPWRITE_PROJECT_ID: str
    APPWRITE_API_KEY_SECRET: str
    Appwrite_API_ENDPOINT: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
    )

settings = Settings()