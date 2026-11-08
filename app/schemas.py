from pydantic import BaseModel, Field, field_validator


class VideoJobRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=4000)

    duration_seconds: int = Field(
        default=5,
        ge=1,
        le=40
    )

    aspect_ratio: str = Field(
        default="16:9",
        pattern=r"^(16:9|9:16|1:1)$"
    )

    resolution: str = Field(
        default="1080p",
        pattern=r"^(720p|1080p)$"
    )

    reference_image_urls: list[str] = Field(
        default_factory=list,
        max_length=30
    )

    @field_validator("prompt")
    @classmethod
    def prompt_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Prompt cannot be blank")
        return value.strip()


class VideoJobCreated(BaseModel):
    job_id: str
    status: str
    message: str


class VideoJobStatus(BaseModel):
    job_id: str
    status: str
    progress: int = 0
    video_url: str | None = None
    error: str | None = None￼Enter
