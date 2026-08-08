from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Aviator Live Data API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Aviator Live Data API",
        "version": "1.0.0",
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/live")
def live():
    """
    Backend test endpoint.

    Replace the test value with data from a source
    that you are authorized to access.
    """

    return {
        "status": "live",
        "value": 1.00,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
