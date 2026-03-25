from sqlalchemy.orm import Session
from models.notification_model import Notification

def create_notification(db: Session, data):
    notification = Notification(
        notification=data.notification,
        created_by=data.created_by,
        user_role=data.user_role,
        user_name=data.user_name
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification