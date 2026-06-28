from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database.db import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, nullable = False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable = False)
    order_status = Column(String(50), default="Pending", nullable = False)
    total_amount = Column(Float, nullable = False)
    created_at = Column(DateTime, server_default=func.now(), nullable = False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    #     # relationship with order and payment table
    payment = relationship("Payments", back_populates = "order", uselist = False)

    # relationship with order and customer table
    customer = relationship("Customers", back_populates = "orders")

    # relatonship with order and order_items table
    order_items = relationship("OrderItems", back_populates = "order")

    def __repr__(self):
        return f"<Order {self.order_id}>"


# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
# from sqlalchemy.orm import relationship
# from database.db import Base

# class Order(Base):
#     __tablename__ = 'orders'

#     order_id = Column(Integer, primary_key = True)
#     customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable = False)
#     order_status = Column(String(50), nullable = False)
#     # food_id = Column(String, ForeignKey('food.food_id'), nullable = False)
#     # quantity = Column(Integer, nullable = False)
#     # total_price = Column(Float, nullable = False)
#     created_at = Column(DateTime, server_default = func.now(), nullable = False)
#     updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)

