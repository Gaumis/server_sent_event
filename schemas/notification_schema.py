from pydantic import BaseModel
from typing import List

class NotificationCreate(BaseModel):
    notification: str
    created_by: str
    user_role: str
    user_name: str

