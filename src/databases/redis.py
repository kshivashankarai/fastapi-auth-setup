import redis.asyncio as aioredis
from src.settings.config import Config

# JTI_EXPIRY defines the time-to-live (TTL) for blocked JWTs (in seconds).
JTI_EXPIRY = 3600

# Create an asynchronous Redis client using the provided Redis URL from the configuration.
token_blocklist = aioredis.from_url(Config.REDIS_URL)


async def add_jti_to_blocklist(jti: str) -> None:
    """
    Adds a JWT ID (JTI) to the blocklist in Redis with an expiration time.
    This effectively blocks the token from being used after it's added.

    :param jti: The JWT ID to be added to the blocklist.
    """
    await token_blocklist.set(name=jti, value="", ex=JTI_EXPIRY)


async def token_in_blocklist(jti: str) -> bool:
    """
    Checks if a JWT ID (JTI) is in the blocklist.

    :param jti: The JWT ID to be checked.
    :return: True if the JTI is in the blocklist, False otherwise.
    """
    jti = await token_blocklist.get(jti)

    return jti is not None
