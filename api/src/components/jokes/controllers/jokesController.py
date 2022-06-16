from typing import List

from ..model.jokeModel import jokeModelResponse
from ..services.jokesService import Service as JockeService


class Controller:

    @staticmethod
    async def getJokes(params) -> List[jokeModelResponse]:
        resp = await JockeService.getJokes(params['source'])
        return resp

    @staticmethod
    async def addJoke(payload) -> List[jokeModelResponse]:
        resp = await JockeService.addJoke(payload)
        return resp

    @staticmethod
    async def updateJoke(jokeId, payload) -> List[jokeModelResponse]:
        resp = await JockeService.updateJoke(jokeId, payload)
        return resp

    @staticmethod
    async def deleteJoke(jokeId) -> List[jokeModelResponse]:
        resp = await JockeService.deleteJoke(jokeId)
        return resp
