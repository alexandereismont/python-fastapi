from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from conf.db_config import Base, engine


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("shop.id"))

    owner = relationship("Shop", back_populates="items")


Item.metadata.create_all(engine)