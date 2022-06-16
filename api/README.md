
# API challenge fastapi

This api is a challange where is use FastApi, python, MongoPy, MongoAtlas, External Apis conecctions for generate random jokes. The API allow generate random, add new joke, update and delete. Also this Api has other endpints that allow calculate MCM of array of numbers and incremente the value of number.



## Installation

How to run api challenge

```bash
  pip install -r requirements.txt
```
So you need to load the seed for this run the following
```bash
  bash api/scripts/seed.sh
```
The for run the API run the following command:
```bash
  bash api/scripts/run.sh
```
After that it start to run the units test and finally it run API
  

#### NOTE: If you want or need run the local mongodb you can run the docker-compose and add the url connection of your mongodb in the environment variables.

## Endpoints Reference api/v1/fastapi/jokes
#### Get random joke
```http
  GET /api/v1/fastapi/jokes
```
| Params      | Type     | Description                |
| :--------   | :------- | :------------------------- |
| `number`    | `str`    | It can be void str, "chuck" or "dad" |

#### Add new joke in database
```http
  POST /api/v1/fastapi/jokes
```
| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `categories` | `[string]` | Category of joke |
| `value`      | `string` | **Required**. content of joke |
| `icon_url`   | `string` | Img icon |
| `url`        | `string` |  Ulr of external api |

#### Update field of joke
```http
  PUT /api/v1/fastapi/jokes${id}
```
| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `categories` | `[string]` | Category of joke |
| `value`      | `string` | content of joke |
| `icon_url`   | `string` | Img icon |
| `url`        | `string` |  Ulr of external api |

#### Delete register of joke
```http
  DELETE /api/v1/fastapi/jokes${id}
```


## Endpoints Reference api/v1/fastapi/calculations
#### Get calculation for MCM of array of numbers
```http
  GET /api/v1/fastapi/calculations/mcm-numbers
```
| Params      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `numbers` | `[string] or string` | numbers to calculate mcm |

```http
  GET /api/v1/fastapi/calculations/increment-number
```
| Params      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `number` | `int` | number for intrement one unity|

```

## Running Tests
To run tests, run the following command

```bash
pytest -v
```