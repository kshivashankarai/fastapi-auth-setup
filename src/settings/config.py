from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database Configuration
    DATABASE_URL: str  # Full Database URL for async operations (e.g., mysql+asyncmy://user:pass@host:port/db)

    # JWT Configuration
    JWT_SECRET: str  # Secret key used for encoding/decoding JWT tokens
    JWT_ALGORITHM: str  # Algorithm used for signing JWT tokens (e.g., HS256)

    # Redis Configuration
    REDIS_URL: str  # Full Redis URL (e.g., redis://localhost:6379/0)

    # Email Configuration
    MAIL_USERNAME: str  # Username for connecting to the mail server
    MAIL_PASSWORD: str  # Password for connecting to the mail server
    MAIL_FROM: str  # Sender's email address
    MAIL_PORT: int  # Mail server port (e.g., 1025 for Mailpit)
    MAIL_SERVER: str  # Mail server address (e.g., localhost)
    MAIL_FROM_NAME: str  # Name to appear as the sender

    # Email Security Configuration
    MAIL_STARTTLS: bool = True  # Use STARTTLS (True if enabled)
    MAIL_SSL_TLS: bool = False  # Use SSL/TLS (True if enabled)
    USE_CREDENTIALS: bool = True  # Whether to use credentials for sending email
    VALIDATE_CERTS: bool = True  # Whether to validate SSL/TLS certificates

    # Application Domain
    DOMAIN: str  # Domain or IP and port where the application is running (e.g., 127.0.0.1:8000)

    # Token Expiry Configuration
    ACCESS_TOKEN_EXPIRY_TIME: str  # Expiry time for access tokens (in minutes)
    REFRESH_TOKEN_EXPIRY_TIME: str  # Expiry time for refresh tokens (in minutes)

    # Internal configuration for Pydantic settings
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Initialize the configuration
Config = Settings()

# Celery or other task queue configurations (if applicable)
broker_url = Config.REDIS_URL  # Broker URL for task queue
result_backend = Config.REDIS_URL  # Backend URL for task results
broker_connection_retry_on_startup = True  # Retry connecting to the broker on startup
