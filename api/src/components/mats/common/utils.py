import json


def sortJsonResponse(jsonResponse):
    return json.loads(json.dumps(jsonResponse, sort_keys=True))
