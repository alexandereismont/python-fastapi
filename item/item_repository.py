from fastapi import Depends
from sqlalchemy.orm import Session

from conf.db_config import get_db
from item.item_model import Item


class ItemRepository:
    db: Session

    def __init__(self, db: Session=Depends(get_db)):
        self.db = db
        pass

    def get_item(self, item_id):
        return self.db.query(Item).filter(Item.id == item_id).first()