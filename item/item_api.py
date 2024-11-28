from fastapi import Depends, APIRouter

from item.item_service import ItemService

router = APIRouter()

class ItemApi:
    item_service: ItemService

    def __init__(self, item_service: Depends(ItemService)):
        self.item_service = item_service