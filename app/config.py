from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    upload_dir: str = "uploads"
    max_reference_images: int = 30
    max_upload_mb: int = 15

    video_provider: str = "mock"
    video_provider_api_key: str = ""
    video_provider_base_url: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
