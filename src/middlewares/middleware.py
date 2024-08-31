from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import time
import logging

# Disable the default Uvicorn access logger to avoid duplicate logging.
logger = logging.getLogger("uvicorn.access")
logger.disabled = True


def register_middleware(app: FastAPI):
    """
    Registers custom middleware to the FastAPI application.

    This function adds a custom logging middleware and two built-in middlewares:
    CORS (Cross-Origin Resource Sharing) middleware and TrustedHost middleware.

    :param app: The FastAPI application instance.
    """

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        """
        A custom logging middleware that logs details about each incoming request,
        including the client's IP, the HTTP method, the URL path, the status code,
        and the time taken to process the request.

        :param request: The incoming request.
        :param call_next: A callable that receives the request and returns the response.
        :return: The response after processing the request.
        """
        start_time = time.time()

        # Process the request and get the response.
        response = await call_next(request)
        processing_time = time.time() - start_time

        # Construct a log message with request details and processing time.
        message = f"{request.client.host}:{request.client.port} - {request.method} - {request.url.path} - {response.status_code} completed after {processing_time}s"

        # Print the log message to the console.
        print(message)
        return response

    # Add CORS middleware to the application.
    # This middleware allows cross-origin requests from any origin ("*").
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow requests from all origins.
        allow_methods=["*"],  # Allow all HTTP methods.
        allow_headers=["*"],  # Allow all headers.
        allow_credentials=True,  # Allow credentials (e.g., cookies, authorization headers).
    )

    # Add TrustedHost middleware to the application.
    # This middleware restricts access to the application to specific hosts.
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=[
            "localhost",
            "127.0.0.1",
        ],  # Only allow these hosts.
    )
