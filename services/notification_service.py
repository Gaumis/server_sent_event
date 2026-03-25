from sqlalchemy.orm import Session
from repo.notification_repo import create_notification
from .redis_service import redis_client
from .sse_service import subscribers
import json

async def save_notification(db: Session, data):
    res = create_notification(db, data)
    # if res:
    #     for queue in subscribers:
    #         await queue.put(res)
    notification_obj = {
        'id': res.id,
        "notification_id": res.notification,
    }
    await redis_client.publish(
        "notifications",
        json.dumps(notification_obj)
    )

    return res
