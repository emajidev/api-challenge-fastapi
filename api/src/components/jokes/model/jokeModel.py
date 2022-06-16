from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from typing import Text


class jokeModelResponse(BaseModel):
    id: str = Field(..., alias="_id")
    categories: Optional[list]
    value: Text
    icon_url: Optional[str]
    url: Optional[str]
    created_at: Optional[str] = str(datetime.now())
    updated_at: Optional[str] = None

    class Config:
        schema_extra = {
            "categories": [],
            "created_at": "2020-01-05 13:42:25.099703",
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "_id": "96tmuEIgSwCbh-OscDPEHA",
            "updated_at": "2020-01-05 13:42:25.099703",
            "url": "https://api.chucknorris.io/jokes/96tmuEIgSwCbh-OscDPEHA",
            "value": "When he was a kid, Chuck Norris' bedroom walls were filled with photos of Chuck Norris."
        }


class jokeModelRequest(BaseModel):
    categories: Optional[list]
    value: Text
    icon_url: Optional[str]
    url: Optional[str]

    class Config:
        schema_extra = {
            "categories": [],
            "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
            "_id": "96tmuEIgSwCbh-OscDPEHA",
            "url": "https://api.chucknorris.io/jokes/96tmuEIgSwCbh-OscDPEHA",
        }
