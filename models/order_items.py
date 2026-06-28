from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database.db import Base


class OrderItems(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, nullable = False)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable = False)
    food_id = Column(String(90), ForeignKey("foods.food_id"), nullable = False)
    quantity = Column(Integer, nullable=False)

    # relationship with order_item and food table
    food = relationship("Food", back_populates = "order_items")

    # relationship with order_item and order table
    order = relationship("Order", back_populates = "order_items")
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default = func.now(), nullable = False)
    updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)

    def __repr__(self):
        return f"<OrderItem {self.order_item_id}>"


# from sqlalchemy import Column, Integer, func, Float, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from database.db import Base


# class OrderItems(Base):
#     __tablename__ = 'order_items'

#     order_item_id = Column(Integer, primary_key = True)
#     order_id = Column(Integer, ForeignKey('orders.order_id'), nullable = False)
#     food_id = Column(Integer, ForeignKey('food.food_id'), nullable = False)
#     quantity = Column(Integer ,nullable = False)



#     price = Column(Float, nullable = False)

