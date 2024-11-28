from fastapi import Depends

from item.item_repository import ItemRepository


class ItemService:
    repository: ItemRepository

    def __init__(self, repository: ItemRepository = Depends(ItemRepository)):
        self.repository = repository
        pass

    def get_item(self, item_id):
        return self.repository.get_item(item_id)