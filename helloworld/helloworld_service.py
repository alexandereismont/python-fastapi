from typing import Annotated

from fastapi import Depends

from helloworld.helloworld_repository import HelloWorldRepository


class HelloWorldService:
    instance = None

    def __new__(cls, repository: HelloWorldRepository = None):
        if cls.instance is None:
            print("Creating the service instance")
            cls.instance = super().__new__(cls)
            cls.instance.repository = repository
        print("Returning the service instance")
        return cls.instance

    def get_message(self):
        return self.repository.get_hello_world()


def get_hello_world_service(
       repository: Annotated[HelloWorldRepository, Depends(HelloWorldRepository)]
) -> HelloWorldService:
    return HelloWorldService(repository=repository)