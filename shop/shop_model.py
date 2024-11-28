from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from conf.db_config import Base, engine


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    stock = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("Item", back_populates="owner")

Shop.metadata.create_all(engine)
