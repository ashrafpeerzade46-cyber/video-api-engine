from datetime import datetime, timezone
from threading import Lock
from uuid import uuid4


class InMemoryJobStore:

    def __init__(self):
        self._jobs = {}
        self._lock = Lock()

    def create(self, payload):
        job_id = str(uuid4())

        job = {
            "job_id": job_id,
            "status": "queued",
            "progress": 0,
            "video_url": None,
            "error": None,
            "payload": payload,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        with self._lock:
            self._jobs[job_id] = job

        return job.copy()

    def get(self, job_id):
        with self._lock:
            job = self._jobs.get(job_id)
            return job.copy() if job else None

    def update(self, job_id, **changes):
        with self._lock:
            job = self._jobs.get(job_id)

            if not job:
                return None

            job.update(changes)
            return job.copy()


jobs = InMemoryJobStore()￼Enter
