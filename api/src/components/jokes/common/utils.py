import json


def sortJsonResponse(jsonResponse) -> dict:
    return json.loads(json.dumps(jsonResponse, sort_keys=True))

