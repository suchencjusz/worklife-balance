import requests
import ujson
from pydantic import BaseModel
import random

def x():
    class ActivityIn(BaseModel):
        id_user: str
        url: str
        unix_timestamp_start: int
        unix_timestamp_end: int
        duration: int

    random_timestamp = random.randint(1633024800, 1635025800)
    duration = random.randint(0, 250)

    # Create an instance of ActivityIn
    activity = ActivityIn(
        id_user="essa",
        url="http://example.com",
        unix_timestamp_start=random_timestamp,
        unix_timestamp_end=random_timestamp + duration,
        duration=duration
    )

    activity_json = activity.model_dump_json()

    # URL of the API endpoint
    url = "http://localhost:8080/api/activities/add"

    requests.post(url, data=activity_json, headers={'Content-Type': 'application/json'})

    print(activity_json)

for i in range(100):
    x()


# Send a POST request with the JSON data
# response = requests.post(url, data=activity_json, headers={'Content-Type': 'application/json'})

# # Print the responseE
# print(response.status_code)
# print(response.text)