import os
import pydantic
import tldextract
import json

from datetime import datetime
from typing import List, Optional

from bson import ObjectId
import bson.json_util as json_util

from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne

from passlib.context import CryptContext

from common.schemas.activity import ActivityIn
from common.schemas.user import User


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

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def migrate(self) -> None:
        self.db.worklife.worklife.create_index(
            [("id_user", 1), ("url", 1)], unique=False
        )
        self.db.worklife.users.create_index([("username", 1)], unique=True)

    def insert_activity(self, ActivityIn: ActivityIn) -> None:
        self.db.worklife.worklife.insert_one(ActivityIn.model_dump())

    def insert_user(self, User: User) -> None:
        try:
            status = self.db.worklife.users.insert_one(User.model_dump())
        except:
            status = False
        return True if status else False

    def get_user(self, username: str) -> Optional[User]:
        data = self.db.worklife.users.find_one({"username": username})

        response = json.loads(json_util.dumps(data))
        return response

    def get_activities(self, id_user: str) -> List[ActivityIn]:
        data = self.db.worklife.worklife.find({"id_user": id_user})

        response = json.loads(json_util.dumps(data))
        return response
    
    def categorize_user_activities(self, id_user: str) -> List[ActivityIn]:

        def extract_domain(url):
            extracted = tldextract.extract(url)
            domain = f"{extracted.domain}.{extracted.suffix}"
            return domain

        activities = self.get_activities(id_user)

        categorized_activities_with_count = {}

        for activity in activities:
            domain = extract_domain(activity["url"])
            if domain in categorized_activities_with_count:
                categorized_activities_with_count[domain] += 1
            else:
                categorized_activities_with_count[domain] = 1

        sea_of_dicts = []

        for key, value in categorized_activities_with_count.items():
            sea_of_dicts.append({"domain": key, "count": value})

        return sea_of_dicts
        
    def sum_user_activities(self, id_user: str) -> List[ActivityIn]:

        def extract_domain(url):
            extracted = tldextract.extract(url)
            domain = f"{extracted.domain}.{extracted.suffix}"
            return domain

        activities = self.get_activities(id_user)

        categorized_activities_with_count = {}

        for activity in activities:
            domain = extract_domain(activity["url"])
            if domain in categorized_activities_with_count:
                categorized_activities_with_count[domain] += activity["duration"]
            else:
                categorized_activities_with_count[domain] = activity["duration"]

        sea_of_dicts = []

        for key, value in categorized_activities_with_count.items():
            sea_of_dicts.append({"domain": key, "duration": value})

        return sea_of_dicts