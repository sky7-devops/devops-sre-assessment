import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator



APP_NAME = os.getenv("APP_NAME", "DevOps SRE Assessment API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "message": APP_NAME,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def info():
    return {
        "application": APP_NAME,
        "version": APP_VERSION
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )