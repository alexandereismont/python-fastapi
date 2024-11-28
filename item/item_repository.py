from fastapi import Depends
from sqlalchemy.orm import Session

from conf.db_config import get_db


class ItemRepository:
    db: Session

    def __init__(self, db: Session=Depends(get_db)):
        self.db = db
        pass

    def get_item(self, item_id):
        pass