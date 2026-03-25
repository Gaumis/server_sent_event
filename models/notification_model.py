from sqlalchemy import Column, Integer, String, DateTime, func
from core.database import Base

class Notification(Base):
    __tablename__ = "notification"
    id = Column(Integer, primary_key=True, index=True)
    notification = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    user_role =Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    last_modified_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())