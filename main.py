import asyncio

from fastapi import FastAPI, Depends, Request
from core.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from controllers.notification_controller import router as notification_router
from core.init_db import init_db
from services.redis_service import redis_listener

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.on_event("startup")
async def startup():
    asyncio.create_task(redis_listener())


app.include_router(notification_router)

# @app.post('/notifications')
# async def notifications(request: Request, db = Depends(get_db)):
#     print("I'm here")
#
#
# @app.get("/test-db")
# def test_db(db: Session = Depends(get_db)):
#     try:
#         result = db.execute(text("SELECT 1"))
#         return {"status": "Connected to Azure PostgreSQL"}
#
#     except Exception as e:
#         return {"status": "Failed", "error": str(e)}