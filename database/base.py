from sqlalchemy.orm import declarative_base
# from db import Base, engine, session_local
# from models.admin import Admin
# from models.customers import Customers
# from models.food import Food
# from models.order import Order
# from models.order_items import OrderItems
# from models.payments import Payments


Base = declarative_base()

# Base.metadata.create_all(bind = engine)
# print("Tables created successfully.")
# db = session_local()

# admin = Admin(
#     admin_id = 1,
#     cust_id = 1
# )

# customer = Customers(
#     cust_id = int(input("Enter customer ID: ")),
#     username = input("Enter username: "),
#     email = input("Enter email: "),
#     password_hash = input("Enter password hash: ")
# )

# food = Food(
#     food_id = 1,
#     food_name = 'Pizza',
#     food_description = 'Delicious cheese pizza',
#     category = 'Main Course',
#     price = 9.99,
#     availability = True,
#     prepare_time = 15
# )

# order_item = OrderItems(
#     order_item_id = 1,
#     order_id = 1,
#     food_id = 1,
#     quantity = 2,
#     Total_price = 19.98
# )

# order = Order(
#     order_id = 1,
#     cust_id = 1,
#     food_id = 1,
#     quantity = 2,
#     total_price = 19.98,
#     order_status = 'Pending'
# )

# payment = Payments(
#     payment_id = 1,
#     order_id = 1,
#     amount = 19.98,
#     payment_method = 'Credit Card',
#     payment_status = 'Completed'
# )

# db.add(admin)
# db.add(customer)
# db.add(food)
# db.add(order_item)
# db.add(order)
# db.add(payment)

# db.commit()

# db.close()