from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.router import api_router
from app.core.logging import setup_logging

from app.core.exceptions import (
    AppException,
    app_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

setup_logging()

app = FastAPI(
    title="AI Cost Intelligence Platform API",
    version="1.0.0"
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

@app.get("/")
def root():
    return {
        "message": "Backend running successfully"
    }