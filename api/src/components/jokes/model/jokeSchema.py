from ..common.utils import sortJsonResponse


def jokeEntity(item) -> dict:
    jsonObj = {}
    for key, value in item.items():
        if(key == '_id'):
            jsonObj[key] = str(value)
        elif(value):
            jsonObj[key] = value
    return sortJsonResponse(jsonObj)


def jokesEntity(entity) -> list:
    return [jokeEntity(item) for item in entity]


    
