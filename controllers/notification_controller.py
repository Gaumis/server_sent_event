from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from sse_starlette import EventSourceResponse

from core.database import get_db
from schemas.notification_schema import NotificationCreate
from services.notification_service import save_notification
from services.sse_service import event_generator

router = APIRouter()

@router.post("/notification")
async def notification(data: NotificationCreate ,db: Session = Depends(get_db)):
    try:
        result = await save_notification(db, data)
        return {
            "message": "Notification created successfully",
            "id": result.id
        }
    except Exception as e:
        return {
            "message": str(e)
        }

@router.get("/notification/stream")
async def stream_notifications():
    return EventSourceResponse(event_generator())