from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str | None = None

class TokenData(BaseModel):
    username: str | None = None
