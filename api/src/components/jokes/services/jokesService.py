from datetime import datetime
import os
import random
from typing import List
from bson.objectid import ObjectId
from dotenv import load_dotenv
from fastapi import HTTPException
from pymongo import ReturnDocument

from src.common.database import conn
from .httpService import Service as httpService
from ..model.jokeModel import jokeModelResponse
from ..common.utils import sortJsonResponse
from ..model.jokeSchema import jokeEntity, jokesEntity

load_dotenv()

CHUCK = str(os.getenv("CHUCK_URL"))
DAD = str(os.getenv("DAD_URL"))


Jokes = conn.jokesdb.jokes

allowSources = ['chuck', 'dad']

jsonResponse = {
    "categories": [],
    "value":  '',
    "icon_url": '',
    "url": '',
    "created_at": '',
    "updated_at": ''
}


class Service:

    @staticmethod
    async def getJokes(source) -> List[jokeModelResponse]:
        await Service.validateAllowSourceValue(source)
        return await Service.actions(source)

    async def actions(source):
        if source:
            actions = {'chuck': Service.chucknorris,
                       'dad': Service.icanhazdadjoke}
            return actions[source.lower()]()

        actionsRandom = [Service.chucknorris,
                         Service.icanhazdadjoke,
                         Service.jokesInLocaldb]

        jsonResponse = random.choice(actionsRandom)()

        return jsonResponse

    def chucknorris():

        chuck = httpService.request(CHUCK)
        chuck["_id"] = chuck.pop("id")
        return [sortJsonResponse(chuck)]

    def icanhazdadjoke():
        resp = httpService.request(DAD)
        jsonResponse['_id'] = resp["id"]
        jsonResponse['value'] = resp["joke"]
        jsonResponse['url'] = DAD
        return [sortJsonResponse(jsonResponse)]

    def jokesInLocaldb():
        randomId = Service.getRandomId()
        jokes = Jokes.find_one({"_id": ObjectId(str(randomId["_id"]))})
        response = jokeEntity(jokes)
        return [response]

    def getRandomId():
        jokes = Jokes.find({}, {'_id': 1})
        ids = jokesEntity(jokes)
        return random.choice(ids)

    async def validateAllowSourceValue(source):
        if source and source.lower() not in allowSources:
            raise HTTPException(
                status_code=403, detail="Source value in path param only allows the values of 'chuck' and 'dad'")

    @staticmethod
    async def addJoke(payload) -> List[jokeModelResponse]:
        jokeId = Jokes.insert_one(payload).inserted_id
        joke = Jokes.find_one({"_id": ObjectId(str(jokeId))})
        response = jokeEntity(joke)
        return [response]

    @staticmethod
    async def updateJoke(jokeId, payload) -> List[jokeModelResponse]:
        payload["updated_at"] = str(datetime.now())
        jokes = Jokes.find_one_and_update(
            {"_id": ObjectId(str(jokeId))},
            {"$set": payload}, return_document=ReturnDocument.AFTER
        )
        response = jokeEntity(jokes)
        return [response]

    @staticmethod
    async def deleteJoke(jokeId) -> List[jokeModelResponse]:
        jokes = Jokes.find_one_and_delete(
            {"_id": ObjectId(str(jokeId))}
        )
        response = jokeEntity(jokes)
        return [response]
