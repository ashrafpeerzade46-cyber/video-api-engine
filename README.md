# Video API Engine

An AI video generation API built with Python and FastAPI.

## Planned Features

- Up to 30 reference image URLs per request
- Video duration requests up to 40 seconds
- 720p and 1080p resolution options
- 16:9, 9:16 and 1:1 aspect ratios
- Video generation job tracking
- API-based video generation provider integration

## Technology

- Python
- FastAPI
- Pydantic
- HTTPX

## Current Status

Backend structure is under development.

The API currently uses a placeholder provider.
Real video generation is not connected yet.

Requested duration, resolution and reference-image limits
will depend on the selected provider's actual capabilities.

## Security

Provider API keys must be stored in environment variables.
Never commit private API keys to this repository.
