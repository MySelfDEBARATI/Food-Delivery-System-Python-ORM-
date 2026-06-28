from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from database.db import Base
from sqlalchemy.orm import relationship


class Food(Base):

    __tablename__ = "foods"

    food_id = Column(String(90), primary_key=True, nullable = False)
    food_name = Column(String(100), nullable = False)
    food_description = Column(String(255), nullable = False)
    category = Column(String(100), nullable = False)
    price = Column(Float, nullable = False)
    quantity = Column(Integer, nullable = False, default = 0)
    availability = Column(Boolean, default = True, nullable = False)
    prepare_time = Column(Integer, nullable = False)

    # relationship with food and order_items table
    order_items = relationship("OrderItems", back_populates = "food")
    created_at = Column(DateTime, server_default = func.now(), nullable = False)
    updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)
    
    def __repr__(self):
        return f"<Food {self.food_name}>"



# from sqlalchemy import  Column, Integer, String, Float, DateTime, Boolean, func
# from sqlalchemy.orm import relationship
# from database.db import Base

# class Food(Base):
#     __tablename__ = 'food'

#     food_id = Column(String(90), primary_key = True)
#     food_name = Column(String(100), nullable = False)
#     food_description = Column(String(255), nullable = False)
#     category = Column(String(50), nullable = False)
#     price = Column(Float, nullable = False)
#     availability = Column(Boolean, default = True, nullable = False)
#     prepare_time = Column(Integer, nullable = False)

