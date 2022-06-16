from ..common.utils import sortJsonResponse


def matEntity(item) -> dict:
    jsonObj = {}
    for key, value in item.items():
        if(key == '_id'):
            jsonObj[key] = str(value)
        elif(value):
            jsonObj[key] = value
    return sortJsonResponse(jsonObj)


def jokesEntity(entity) -> list:
    return [matEntity(item) for item in entity]
