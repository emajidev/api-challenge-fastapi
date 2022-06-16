
from pydantic import BaseModel


class matModelResponse(BaseModel):
    result: int

    class Config:
        schema_extra = {
            "result": 12
        }
