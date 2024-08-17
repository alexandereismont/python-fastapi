from datetime import datetime

from fastapi import Depends
from sqlalchemy import text, select
from sqlalchemy.orm import Session

from conf.db_config import get_db, engine
from shop.dto.ShopDto import ShopDto
from shop.shop_model import Shop


class ShopRepository:

    def __init__(self, db: Session=Depends(get_db)):
        self.db = db
        print("Creating the repository instance")
        pass

    def get_shop(self, shop_id):
        with engine.connect() as connection:
            query = text("select * from shop s where s.id = :id")
            result = connection.execute(statement=query, parameters={"id": shop_id}).fetchone()
        return f"Shop {result.id} from repository!"

    def get_shop_crud(self, shop_id: int):
        stmt = select(Shop).where(shop_id == Shop.id)
        result: Shop = self.db.execute(stmt).first()[0]
        return f"Shop {result.id} from repository!"

    def create_shop(self, shop: ShopDto):
        shop = Shop(**shop.model_dump(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        self.db.add(shop)
        self.db.commit()
        self.db.refresh(shop)
        return f"Shop {shop.name} created in repository!"