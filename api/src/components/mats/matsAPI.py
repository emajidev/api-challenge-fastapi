from typing import List
from fastapi import APIRouter, HTTPException
import ast
from src.middlewares.authMiddleware import token_auth_scheme
from .controllers.matController import Controller
from .model.matModel import matModelResponse
router = APIRouter(
    prefix="/calculations",
    tags=["calculations"],
    responses={404: {"description": "Not found"}},
)


@router.get("/mcm-numbers", response_model=matModelResponse)
async def calculate_mcm(numbers: str):
    if not numbers:
        raise HTTPException(
            status_code=403, detail="The numbers cannot be null and void")

    list = ast.literal_eval(numbers)
    resp = await Controller.calMcm(list)
    return {"result": resp}


@router.get("/increment-number", response_model=matModelResponse)
async def increment_number(number: int):
    if not number:
        raise HTTPException(
            status_code=403, detail="The number cannot be null and void")

    resp = await Controller.incNumber(number)
    return {"result": resp}
