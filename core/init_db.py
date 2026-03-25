from core.database import engine, Base
from models.notification_model import Notification

def init_db():
    Base.metadata.create_all(engine)