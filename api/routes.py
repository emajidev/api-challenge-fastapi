import os
from dotenv import load_dotenv
from fastapi import APIRouter
from src.components.jokes import jokesAPI as jokesRoutes
from src.components.mats import matsAPI as matsRoutes
load_dotenv()

BASE_PATH = str(os.getenv("BASE_PATH"))
routers = APIRouter(
    prefix=BASE_PATH,
)
routers.include_router(jokesRoutes.router)
routers.include_router(matsRoutes.router)
