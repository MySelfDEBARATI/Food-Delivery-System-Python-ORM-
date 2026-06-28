from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from database.db import Base


class Admin(Base):
    __tablename__ = 'admin'

    admin_id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable = False)
    created_at = Column(DateTime, server_default = func.now(), nullable = False)
    updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)

# print("Tables created successfully.")