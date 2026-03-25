import redis.asyncio as redis

from services.sse_service import subscribers

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

async def redis_listener():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("notifications")

    async for message in pubsub.listen():
        if message["type"] == "message":
            notification = message["data"]

            for queue in subscribers:
                await queue.put(notification)