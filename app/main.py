fromfrom fastapi import FastAPI, HTTPException

from app.config import settings
from app.jobs import jobs
from app.provider import video_provider, ProviderNotConfigured
from app.schemas import VideoJobRequest, VideoJobCreated, VideoJobStatus


app = FastAPI(
    title="Video API Engine",
    description="AI video generation API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Video API Engine is running!",
        "environment": settings.app_env
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/video/jobs", response_model=VideoJobCreated)
def create_video_job(request: VideoJobRequest):

    job = jobs.create(request.model_dump())

    try:
        video_provider.generate_video(request.model_dump())
    except ProviderNotConfigured:
        jobs.update(
            job["job_id"],
            status="failed",
            error="Video provider is not configured yet."
        )

    return VideoJobCreated(
        job_id=job["job_id"],
        status="failed",
        message="Job created, but generation requires a real video provider."
    )


@app.get("/video/jobs/{job_id}", response_model=VideoJobStatus)
def get_video_job(job_id: str):

    job = jobs.get(job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Video job not found"
        )

    return VideoJobStatus(
        job_id=job["job_id"],
        status=job["status"],
        progress=job["progress"],
        video_url=job["video_url"],
        error=job["error"]
    )￼Enter
