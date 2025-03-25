# database/redis.py
from redis.asyncio import Redis
from typing import AsyncGenerator
import os

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

async def get_redis() -> AsyncGenerator[Redis, None]:
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    try:
        yield redis_client
    finally:
        await redis_client.close()