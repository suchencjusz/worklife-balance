import requests
import ujson
from pydantic import BaseModel

class ActivityIn(BaseModel):
    id_user: str
    url: str
    unix_timestamp_start: int
    unix_timestamp_end: int

# Create an instance of ActivityIn
activity = ActivityIn(
    id_user="user123",
    url="http://example.com",
    unix_timestamp_start=1633024800,  # Example timestamp
    unix_timestamp_end=1633028400     # Example timestamp
)

activity_json = activity.model_dump_json()

# URL of the API endpoint
url = "http://localhost:8080/api/activities/add"

# Send a POST request with the JSON data
response = requests.post(url, data=activity_json, headers={'Content-Type': 'application/json'})

# Print the responseE
print(response.status_code)
print(response.text)