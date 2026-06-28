from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database.db import Base

class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key = True, nullable = False)
    username = Column(String(50), nullable = False, unique = True)
    phone_no = Column(String(10), nullable = False, unique = True)
    email = Column(String(100), nullable = False, unique = True)
    address = Column(String(255), nullable = False)
    # relationship with customer and order table
    orders = relationship("Order", back_populates = "customer", cascade = "all, delete-orphan")
    password_hash = Column(String(255), nullable = False)
    role = Column(String(20), default="customer", nullable = False)
    created_at = Column(DateTime, server_default = func.now(), nullable = False)
    updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)