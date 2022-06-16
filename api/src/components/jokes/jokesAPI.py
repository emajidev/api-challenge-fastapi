from typing import List
from fastapi import APIRouter, status, Response, Depends
from .model.jokeModel import jokeModelResponse, jokeModelRequest

from src.middlewares.authMiddleware import token_auth_scheme
from .controllers.jokesController import Controller


router = APIRouter(
    prefix="/jokes",
    tags=["jokes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[jokeModelResponse])
async def get_jokes(source: str = None) -> Response:
    params = {"source": source}
    resp = await Controller.getJokes(params)
    return resp


@router.post("/", response_model=List[jokeModelResponse])
async def add_joke(body: jokeModelRequest, response: Response) -> Response:
    response.status_code = status.HTTP_201_CREATED
    body = dict(body)
    resp = await Controller.addJoke(body)
    return resp


@router.put("/{id}", response_model=List[jokeModelResponse])
async def update_joke(id: str, body: dict) -> Response:
    body = dict(body)
    resp = await Controller.updateJoke(id, body)
    return resp


@router.delete("/{id}")
async def delete_joke(id: str) -> Response:
    resp = await Controller.deleteJoke(id)
    return resp
""" taken: str = Depends(token_auth_scheme) """
