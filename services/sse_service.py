import asyncio

subscribers = []

async def event_generator():
    queue = asyncio.Queue()
    subscribers.append(queue)
    try:
        while True:
            data = await queue.get()
            yield {
                "event": "notification",
                "data": data
            }
    finally:
        subscribers.remove(queue)