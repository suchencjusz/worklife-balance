from common.schemas.activity import ActivityIn
from database.DB import DB
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/activities")


@router.post("/add")
async def add_activity(activity: ActivityIn) -> JSONResponse:
    DB.insert_activity(activity)
    return JSONResponse({"status": "ok"})


@router.get("/get_user/{id_user}")
async def get_activities(id_user: str) -> JSONResponse:
    activities = DB.get_activities(id_user)
    return JSONResponse({"activities": activities})


@router.get("/most_visited_domains/{id_user}")
async def get_most_visited_domains(id_user: str) -> JSONResponse:
    activities = DB.categorize_user_activities(id_user)
    return JSONResponse({"activities": activities})


@router.get("/sum_visited_domains/{id_user}")
async def get_sum_visited_domains(id_user: str) -> JSONResponse:
    activities = DB.sum_user_activities(id_user)
    return JSONResponse({"activities": activities})
