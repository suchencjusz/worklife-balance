from database.DB import DB
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from common.schemas.activity import ActivityIn

router = APIRouter(prefix="/api/activities")

@router.post("/add")
async def add_activity(activity: ActivityIn) -> JSONResponse:
    
    DB.insert_activity(activity)
    return JSONResponse({"status": "ok"})
