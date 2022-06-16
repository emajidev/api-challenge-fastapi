
import os
from fastapi.testclient import TestClient
from app import app
from dotenv import load_dotenv

from .model.jokeModel import jokeModelResponse

client = TestClient(app)
load_dotenv()

CHUCK = str(os.getenv("CHUCK_URL"))
DAD = str(os.getenv("DAD_URL"))
BASE_PATH = str(os.getenv("BASE_PATH"))


def test_get_jokes_endpoint():
    response = client.get(BASE_PATH+"/jokes",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert verifyResponseWithSchema(response.json())


def test_get_jokes_endpoint_chuck():
    response = client.get(BASE_PATH+"/jokes?source=chuck",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert verifyResponseWithSchema(response.json())
    assert validateSource(response.json(), CHUCK)


def test_get_jokes_endpoint_dad():
    response = client.get(BASE_PATH+"/jokes?source=dad",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert verifyResponseWithSchema(response.json())
    assert validateSource(response.json(), DAD)


def test_post_put_delete_endpoint():
    joke = {
        "value": "test joke"
    }
    response = client.post(BASE_PATH+"/jokes/", json=joke)
    id = response.json()[0]["_id"]
    assert response.status_code == 201
    assert True if type(id) is str else False
    test_put_endpoint(id)


def test_put_endpoint(id):
    joke = {
        "value": "update test joke"
    }
    url = BASE_PATH+"/jokes/"+id
    response = client.put(url, json=joke)
    assert response.status_code == 200
    assert response.json()[0]["value"] == joke["value"]
    test_delete_endpoint(url)


def test_delete_endpoint(url):
    response = client.delete(url)
    assert response.status_code == 200


def verifyResponseWithSchema(dic) -> jokeModelResponse:
    resp = dic[0]
    exitsInSchema = jokeModelResponse(**resp)  # Discarded or not accepted
    if(exitsInSchema):
        return True
    return False


def validateSource(response, url):
    for item in response:
        if item['url'] == url:
            True
        else:
            False
