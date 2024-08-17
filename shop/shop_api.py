from typing import Annotated

from fastapi import FastAPI, APIRouter, Depends
from fastapi_utils.cbv import cbv

from shop.dto.ShopDto import ShopDto
from shop.shop_repository import ShopRepository
from shop.shop_service import ShopService

router = APIRouter()

def _create_shop_service(repository: Annotated[ShopRepository, Depends(ShopRepository)]) -> ShopService:
   # return ShopService(repository=repository)
    pass


@cbv(router)
class ShopApi:
    service: ShopService = Depends(ShopService)

    @router.get("/shop/{shop_id}")
    def get_shop(self, shop_id: int):
        return self.service.get_shop(shop_id=shop_id)

    @router.post("/shop")
    def create_shop(self, shop: ShopDto):
        return self.service.create_shop(shop=shop)

# , service: Annotated[ShopService, Depends(_create_shop_service)]