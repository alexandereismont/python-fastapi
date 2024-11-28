from typing import Annotated

from fastapi import Depends, FastAPI

from helloworld.helloworld_service import HelloWorldService, get_hello_world_service
from item import item_api
from shop import shop_api

app = FastAPI()

app.include_router(shop_api.router)
app.include_router(item_api.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/message")
def get_message(service: Annotated[HelloWorldService, Depends(get_hello_world_service)]):
    return service.get_message()
