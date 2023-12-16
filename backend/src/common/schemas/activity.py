from pydantic import BaseModel

class ActivityIn(BaseModel):
    _id: str
    id_user: str
    url: str
    unix_timestamp_start: int
    unix_timestamp_end: int
    duration: int
