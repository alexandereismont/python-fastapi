from fastapi import Depends, APIRouter

from item.item_service import ItemService

router = APIRouter()

class ItemApi:
    item_service: ItemService

    def __init__(self, item_service: Depends(ItemService)):
        self.item_service = item_service

    @router.get("/items/{item_id}")
    def get_shop(self, item_id: int):
        return self.item_service.get_item(item_id=item_id)