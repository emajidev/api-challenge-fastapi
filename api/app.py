import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import routers as apiRouters
load_dotenv()

app = FastAPI(debug=str(os.getenv("DEBBUGING")),
              title="API CHALLENGE FAST API",
              description="Challenge about fatapi to test the knowledge of API REST and python ",
              version="0.0.1",
              contact={
                  "name": "Emanuel Jimenez",
                  "email": "emajidev@gmail.com",
                  "phone": "+58-0414.022.08.46"
},
    license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
},)


@app.get('/')
def welcome():
    return {"welcome": "API challenge"}


app.include_router(apiRouters)
