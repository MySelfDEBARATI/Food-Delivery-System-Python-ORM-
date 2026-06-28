from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database.db import Base


class Payments(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True,  nullable = False)

    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable = False)

    amount = Column(Float, nullable=False)

    payment_method = Column(String(50), nullable = False)

    payment_status = Column(String(50), nullable = False)

    # relationship with payment and order table
    order = relationship("Order", back_populates = "payment")

    created_at = Column(DateTime, server_default = func.now(), nullable = False)
    updated_at = Column(DateTime, server_default = func.now(), onupdate = func.now(), nullable = False)

    def __repr__(self):
        return f"<Payment {self.payment_id}>"
    



# from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, func
# from sqlalchemy.orm import relationship
# from database.db import Base

# class Payments(Base):
#     __tablename__ = 'payments'

#     payment_id = Column(Integer, primary_key = True)
#     order_id = Column(Integer, ForeignKey('orders.order_id'), nullable = False)
#     amount = Column(Float, nullable = False)
#     payment_method = Column(String(50), nullable = False)
#     payment_status = Column(String(50), nullable = False)
