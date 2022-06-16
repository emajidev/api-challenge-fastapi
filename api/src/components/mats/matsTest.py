
import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

load_dotenv()
BASE_PATH = str(os.getenv("BASE_PATH"))



def test_get_calculate_mcm():

    response = client.get(BASE_PATH+"/calculations/mcm-numbers?numbers=2,4,6",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "result": 12,
    }


def test_get_calculate_increment():
    response = client.get(BASE_PATH+"/calculations/increment-number?number=5",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "result": 6,
    }
