from fastapi import Depends

from shop.dto.ShopDto import ShopDto
from shop.shop_repository import ShopRepository


class ShopService:
    instance = None
    _repository: ShopRepository

    def __init__(self, repository: ShopRepository = Depends(ShopRepository)):
        self._repository = repository
        print("Creating the service instance")
        pass

    def get_shop(self, shop_id):
        return self._repository.get_shop_crud(shop_id)

    def create_shop(self, shop: ShopDto):
        return self._repository.create_shop(shop)
