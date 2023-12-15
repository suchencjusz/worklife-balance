import os
from datetime import datetime
from typing import List

import pydantic
from bson import ObjectId
# from database.queryCreator import sorting_query_creator
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne

from common.schemas.activity import ActivityIn


class DBClient:
    def __init__(self) -> None:
        # pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

        load_dotenv()
        DB_URI = os.environ.get("DB_URI", "")
        if DB_URI is None:
            raise Exception("DB_URI is not defined")

        self.client = MongoClient(DB_URI)
        self.db = self.client
        self.migrate()

    def migrate(self) -> None:
        self.db.worklife.worklife.create_index(
            [("id_user", 1), ("url", 1)], unique=False
        )

    def insert_activity(self, ActivityIn: ActivityIn) -> None:

        self.db.worklife.worklife.insert_one(ActivityIn.model_dump())

    def get_activities(self, id_user: str) -> List[ActivityIn]:
        activities = self.db.worklife.worklife.find({"id_user": id_user})
        return [ActivityIn(**activity) for activity in activities]