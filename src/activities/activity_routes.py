from database.DB import DB
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from common.schemas.activity import ActivityIn

router = APIRouter(prefix="/api/activities")

@router.post("/add")
async def add_activity(activity: ActivityIn) -> JSONResponse:
    
    DB.insert_activity(activity)
    return JSONResponse({"status": "ok"})

@router.get("/get_user/{id_user}")
async def get_activities(id_user: str) -> JSONResponse:
    activities = DB.get_activities(id_user)
    return JSONResponse({"activities": activities})
