from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from src.settings.config import Config

# Create an asynchronous SQLAlchemy engine using the database URL from the configuration.
async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL))


# Asynchronous function to initialize the database.
async def init_db() -> None:
    """
    Initializes the database by creating all tables defined in the SQLModel's metadata.
    """
    # Begin a connection to the database.
    async with async_engine.begin() as conn:
        # Run the SQLModel's create_all method to create all tables.
        await conn.run_sync(SQLModel.metadata.create_all)


# Asynchronous function to get a session for database operations.
async def get_session() -> AsyncSession:
    """
    Provides an asynchronous session for interacting with the database.
    This session is used within a context manager, ensuring it is properly closed after use.
    """
    # Create a sessionmaker bound to the async engine.
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    # Provide the session within a context manager.
    async with Session() as session:
        yield session
