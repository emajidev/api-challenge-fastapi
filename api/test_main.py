import os
import sys
from dotenv import load_dotenv
from fastapi.testclient import TestClient
import pytest

from app import app

from src.components.jokes.jokesTest import test_get_jokes_endpoint, test_post_put_delete_endpoint
from src.components.mats.matsTest import test_get_calculate_mcm, test_get_calculate_increment
client = TestClient(app)

load_dotenv()
BASE_PATH = str(os.getenv("DAD_URL"))



def test_verify_up_api():
    response = client.get(BASE_PATH, headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {"welcome": "API challenge"}


test_get_jokes_endpoint
test_post_put_delete_endpoint
test_get_calculate_mcm
test_get_calculate_increment
