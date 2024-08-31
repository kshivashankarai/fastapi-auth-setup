from fastapi import FastAPI
from src.modules.auth.routes import auth_router
from src.modules.books.routes import book_router
from .errors.errors import register_all_errors
from .middlewares.middleware import register_middleware

# Define the version of the API.
version = "v1.0.0"

# Provide a brief description of the application.
description = """Visa Management Module"""

# Define the prefix for versioning the API routes.
version_prefix = "/api/{version}"

# Create an instance of the FastAPI application.
app = FastAPI(
    title="VMS",  # Title of the application.
    description=description,  # Description of the application.
    version=version,  # Version of the application.
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit",
    },  # License information.
    contact={
        "name": "Shiva Shankar K",  # Contact name.
        "url": "https://www.exalogic.co/",  # Contact URL.
        "email": "shiva.shankar@exalogic.co",  # Contact email.
    },
    openapi_url=f"{version_prefix}/openapi.json",  # URL for OpenAPI schema.
    docs_url=f"{version_prefix}/docs",  # URL for automatic documentation (Swagger UI).
    redoc_url=f"{version_prefix}/redoc",  # URL for ReDoc documentation.
)

# Register custom error handlers to the application.
register_all_errors(app)

# Register custom middleware to the application.
register_middleware(app)

# Include the authentication router with a versioned prefix and appropriate tags for documentation.
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])

# Include the books router with a versioned prefix and appropriate tags for documentation.
app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
