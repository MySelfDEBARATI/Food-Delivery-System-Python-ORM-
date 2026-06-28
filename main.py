from database.db import Base, engine
from models import *
from database.db import session_local
import getpass
import bcrypt


# input field mandatory function

def get_required_input(message):

    while True:

        value = input(message).strip()

        if value == "":
            print(
                "Error: Input field is mandatory."
            )
            continue

        return value
    
# integer input field miss kore gele
    
def get_int_input(message):

    while True:

        value = get_required_input(message)

        try:
            return int(value)

        except ValueError:
            print(
                "Please enter a valid number."
            )

# float input field miss kore gele

def get_float_input(message):

    while True:

        value = get_required_input(message)

        try:
            return float(value)

        except ValueError:
            print(
                "Please enter a valid amount."
            )

# food data with column name display koranor function

def display_food_table(foods):

    print("\n" + "=" * 110)

    print(
        f"{'ID':<5}"
        f"{'FOOD NAME':<25}"
        f"{'CATEGORY':<20}"
        f"{'PRICE':<10}"
        f"{'QTY':<10}"
        f"{'AVAILABLE':<15}"
    )

    print("=" * 110)

    for food in foods:

        print(
            f"{food.food_id:<5}"
            f"{food.food_name:<25}"
            f"{food.category:<20}"
            f"{food.price:<10}"
            f"{food.quantity:<10}"
            f"{str(food.availability):<15}"
        )

    print("=" * 110)

# database utilization

Base.metadata.create_all(bind=engine)
# print("Tables Created Successfully")


session = session_local()

existing_admin = (
    session.query(Customers)
    .filter(Customers.username == "admin")
    .first()
)

if existing_admin:
    pass
else:
    admin = Customers(
        username="admin",
        email="admin@gmail.com",
        phone_no="8420639416",
        address="Office",
        password_hash="admin123",
        role="admin"
    )

    session.add(admin)
    session.commit()

    print("Admin Created Successfully")

session.close()

# registration section start

def register():
    session = session_local()

    username = get_required_input("Username: ")
    email = get_required_input("Email: ")
    phone = get_required_input("Phone: ")
    address = get_required_input("Address: ")
    # role = input("Role: ")
    password = get_required_input("Password: ")

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


    customer = Customers(
        username=username,
        email=email,
        phone_no=phone,
        address=address,
        # role = role
        password_hash=hashed_password,
    )

    session.add(customer)
    session.commit()

    print("Registration successful")

    session.close()

# registration close 


# login section start

def login():
    session = session_local()

    role = get_required_input("Role (admin/customer): ").lower()

    if role == "admin" or role == "customer":
        username = get_required_input("Username: ")
        password = get_required_input("Password: ")

        user = (
            session.query(Customers).filter(
                Customers.username == username,
                Customers.role == role,
            ).first()
        )
    
        if user and bcrypt.checkpw(
            password.encode(),
            user.password_hash.encode()
        ):        
            session.close()
            return user
        
        print("Invalid Username or Password")
        session.close()
        return None

    else:
        print("Invalid choice. Please enter a valid role to login.")
        session.close()
        return None

# Login closed


# Add food function

def add_food():

    session = session_local()

    try:
        food_id = get_required_input("Food ID: ")
        existing_food = (session.query(Food).filter(Food.food_id == food_id).first())

        if existing_food:
            print("Food ID already exists.")
            return

        food_name = get_required_input("Food Name: ")
        description = get_required_input("Description: ")
        category = get_required_input("Category: ")
        price = get_float_input("Price: ")
        quantity = get_int_input("Quantity: ")
        prepare_time = get_int_input("Preparation Time (minutes): ")
        availability_input = (get_required_input("Available (yes/no): ").lower())
        availability = (availability_input == "yes")

        food = Food(
            food_id=food_id,
            food_name=food_name,
            food_description=description,
            category=category,
            price=price,
            quantity=quantity,
            availability=availability,
            prepare_time=prepare_time
        )

        session.add(food)
        session.commit()

        print("Food Added Successfully")

    except Exception as e:
        session.rollback()
        print(e)

    finally:
        session.close()

# Add food closed


# View food function

def view_foods():

    session = session_local()
    foods = session.query(Food).all()

    if not foods:
        print("No Food Available")

    else:
        display_food_table(foods)

    session.close()

# View food closed


# Update food function

def update_food():

    session = session_local()
    view_foods()

    food_id = get_required_input("Enter Food ID: ")

    food = (
        session.query(Food)
        .filter(Food.food_id == food_id)
        .first()
    )

    if not food:
        print("Food Not Found")

        session.close()
        return

    print("\nCurrent Details")
    print(f"Name: {food.food_name}")
    print(f"Description: {food.food_description}")
    print(f"Category: {food.category}")
    print(f"Price: {food.price}")
    print(f"Quantity: {food.quantity}")
    print(f"Availability: {food.availability}")
    print(f"Preparation Time: {food.prepare_time}")
    print("\nEnter New Values")

    food.food_name = get_required_input("Food Name: ")
    food.food_description = (get_required_input("Description: "))
    food.category = (get_required_input("Category: "))
    food.price = get_float_input("Price: ")
    food.quantity = get_int_input("Quantity: ")
    food.prepare_time = (get_int_input("Preparation Time: "))
    availability = (get_required_input("Available (yes/no): ").lower())
    food.availability = (availability == "yes")

    session.commit()

    print("Food Updated Successfully")

    session.close()

# Update food closed


# Delete food function

def delete_food():

    session = session_local()

    food_id = get_required_input("Food ID: ")

    food = (
        session.query(Food)
        .filter(Food.food_id == food_id)
        .first()
    )

    if food is None:
        print("Food Not Found")

    else:
        session.delete(food)
        session.commit()

        print("Food Deleted Successfully")

    session.close()

# Delete food closed


# View orders function

def view_orders():

    session = session_local()

    orders = session.query(Order).all()

    if not orders:

        print("No Orders Found")

        session.close()
        return

    print("\n" + "=" * 120)

    print(
        f"{'ORDER ID':<10}"
        f"{'CUSTOMER':<12}"
        f"{'FOOD ID':<10}"
        f"{'QTY':<8}"
        f"{'PRICE':<12}"
        f"{'STATUS':<20}"
    )

    print("=" * 120)

    for order in orders:

        items = (
            session.query(OrderItems)
            .filter(
                OrderItems.order_id
                == order.order_id
            )
            .all()
        )

        for item in items:

            print(
                f"{order.order_id:<10}"
                f"{order.customer_id:<12}"
                f"{item.food_id:<10}"
                f"{item.quantity:<8}"
                f"{item.price:<12}"
                f"{order.order_status:<20}"
            )

    print("=" * 120)

    session.close()

# View orders closed


# Update order status function

def update_order_status():

    session = session_local()

    view_orders()

    order_id = get_int_input(
        "Enter Order ID: "
    )

    order = (
        session.query(Order)
        .filter(
            Order.order_id
            == order_id
        )
        .first()
    )

    if not order:

        print(
            "Order Not Found"
        )

        session.close()
        return

    print(
        f"\nCurrent Status : "
        f"{order.order_status}"
    )

    print("\nChoose Status")

    print("1. Pending")
    print("2. Preparing")
    print("3. Out For Delivery")
    print("4. Delivered")
    print("5. Cancelled")

    choice = get_required_input(
        "Choice: "
    )

    status_map = {

        "1": "Pending",
        "2": "Preparing",
        "3": "Out For Delivery",
        "4": "Delivered",
        "5": "Cancelled"
    }

    if choice not in status_map:

        print("Invalid Choice")

        session.close()
        return

    order.order_status = (
        status_map[choice]
    )

    session.commit()

    print(
        "Order Status Updated Successfully"
    )

    session.close()

# Update order status closed


# Admin menu section start

def admin_menu():

    while True:
        print("\n" + "=" * 30)
        print("         Admin Menu")
        print("=" * 30)

        print("1. Add Food")
        print("2. View Foods")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. View Orders")
        print("6. Update Order Status")
        print("7. Logout")

        choice = input("Enter choice.")

        if choice == "1":
            add_food()
        
        elif choice == "2":
            view_foods()

        elif choice == "3":
            update_food()
        
        elif choice == "4":
            delete_food()
        
        elif choice == "5":
            view_orders()
        
        elif choice == "6":
            update_order_status()
        
        elif choice == "7":
            print("Admin Successfully Logged Out.")
            break

        else:
            print("Invalid Choice") 

# Admin menu closed


# Place order function

def place_order(customer_id):

    session = session_local()

    foods = (
        session.query(Food)
        .filter(
            Food.availability == True,
            Food.quantity > 0
        )
        .all()
    )

    if not foods:
        print("No Food Available")
        session.close()
        return

    display_food_table(foods)

    food_name = get_required_input("\nEnter Food Name: ")

    food = (
        session.query(Food).filter(Food.food_name.ilike(food_name)).first())

    if food is None:
        print("Food Not Found")

        session.close()
        return

    quantity = get_int_input("Quantity: ")

    if quantity <= 0:
        print("Quantity must be greater than zero.")

        session.close()
        return

    if quantity > food.quantity:
        print(f"Only {food.quantity} item(s) available.")

        session.close()
        return

    total_price = food.price * quantity

    order = Order(
        customer_id=customer_id,
        order_status="Pending",
        total_amount=total_price
    )

    session.add(order)
    session.commit()

    order_item = OrderItems(
        order_id=order.order_id,
        food_id=food.food_id,
        quantity=quantity,
        price=total_price
    )

    session.add(order_item)

    food.quantity -= quantity

    if food.quantity == 0:
        food.availability = False

    session.commit()

    print("\n" + "=" * 50)
    print("ORDER PLACED SUCCESSFULLY")
    print("=" * 50)

    print(f"Food Name   : {food.food_name}")
    print(f"Quantity    : {quantity}")
    print(f"Unit Price  : ₹{food.price}")
    print(f"Total Amount: ₹{total_price}")
    print(f"Order ID    : {order.order_id}")
    print("=" * 50)

    session.close()

# Place order function closed


# View my orders function

def view_my_orders(customer_id):

    session = session_local()

    orders = (session.query(Order).filter(Order.customer_id == customer_id).all())

    if not orders:
        print("No Orders Found")

        session.close()
        return

    print("\n" + "=" * 120)

    print(
        f"{'ORDER ID':<10}"
        f"{'FOOD NAME':<25}"
        f"{'QTY':<10}"
        f"{'TOTAL':<12}"
        f"{'STATUS':<22}"
    )

    print("=" * 120)

    for order in orders:
        items = (session.query(OrderItems).filter(OrderItems.order_id == order.order_id).all())

        for item in items:
            food = (session.query(Food).filter(Food.food_id == item.food_id).first())

            print(
                f"{order.order_id:<10}"
                f"{food.food_name:<25}"
                f"{item.quantity:<10}"
                f"₹{order.total_amount:<11}"
                f"{order.order_status:<22}"
            )

    print("=" * 120)

    session.close()

# View my orders closed


# Payment function

def payment(customer_id):

    session = session_local()

    orders = (
        session.query(Order)
        .filter(Order.customer_id == customer_id,Order.order_status != "Cancelled").all()
    )

    if not orders:
        print("No Orders Available For Payment")

        session.close()
        return

    print("\n" + "=" * 100)
    print(
        f"{'ORDER ID':<10}"
        f"{'FOOD NAME':<20}"
        f"{'QTY':<8}"
        f"{'TOTAL':<12}"
        f"{'STATUS':<20}"
    )
    print("=" * 100)

    for order in orders:
        item = (
            session.query(OrderItems)
            .filter(OrderItems.order_id == order.order_id).first()
        )

        food = (
            session.query(Food)
            .filter(Food.food_id == item.food_id).first()
        )

        print(
            f"{order.order_id:<10}"
            f"{food.food_name:<20}"
            f"{item.quantity:<8}"
            f"₹{order.total_amount:<11}"
            f"{order.order_status:<20}"
        )
    print("=" * 100)

    order_id = get_int_input("\nEnter Order ID: ")

    order = (
        session.query(Order)
        .filter(Order.order_id == order_id,Order.customer_id == customer_id).first()
    )

    if order is None:
        print("Invalid Order ID")

        session.close()
        return
    
    existing_payment = (session.query(Payments).filter(Payments.order_id == order.order_id,
        Payments.payment_status == "Payment Successful").first())

    if existing_payment:
        print("Payment Already Completed.")

        session.close()
        return
    
    print("\nChoose Payment Method\n")
    print("1. Google Pay")
    print("2. PhonePe")
    print("3. Paytm")
    print("4. Card Payment")
    print("5. Cash On Delivery")
    
    choice = get_required_input("Choice: ")

    if choice == "1":
        payment = Payments(
            order_id=order.order_id,
            amount=order.total_amount,
            payment_method="Google Pay",
            payment_status="Payment Successful"
        )
        session.add(payment)
        session.commit()
        print("\nPayment Successful")
    
    elif choice == "2":
        payment = Payments(
            order_id=order.order_id,
            amount=order.total_amount,
            payment_method="PhonePe",
            payment_status="Payment Successful"
        )
        session.add(payment)
        session.commit()
        print("\nPayment Successful")

    elif choice == "3":
        payment = Payments(
            order_id=order.order_id,
            amount=order.total_amount,
            payment_method="Paytm",
            payment_status="Payment Successful"
        )
        session.add(payment)
        session.commit()
        print("\nPayment Successful")

    elif choice == "4":
        card_number = get_required_input("Enter Card Number: ")
        if len(card_number) != 16 or not card_number.isdigit():
            print("Invalid Card Number")
            session.close()
            return
        pin = getpass.getpass("Enter 4 Digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN")
            session.close()
            return
    
        payment = Payments(
            order_id=order.order_id,
            amount=order.total_amount,
            payment_method="Card",
            payment_status="Payment Successful"
        )
        session.add(payment)
        session.commit()
        print("\nCard Payment Successful")

    elif choice == "5":
        payment = Payments(
            order_id=order.order_id,
            amount=order.total_amount,
            payment_method="Cash On Delivery",
            payment_status="Pending"
        )
        session.add(payment)
        session.commit()
        print("\nCash On Delivery Selected")
        print(f"Amount Payable : ₹{order.total_amount}")

    else:
        print("Invalid Choice")
    
    session.close()

# Payment closed


# Cancel orders function

def cancel_order(customer_id):

    session = session_local()

    orders = (session.query(Order).filter(Order.customer_id == customer_id).all())

    if not orders:
        print("No Orders Found")
        session.close()
        return

    view_my_orders(customer_id)

    order_id = get_int_input("\nEnter Order ID to Cancel: ")

    order = (
        session.query(Order)
        .filter(Order.order_id == order_id, Order.customer_id == customer_id).first()
    )

    if order is None:
        print("Order Not Found")
        session.close()
        return

    # Already Cancelled

    if order.order_status == "Cancelled":
        print("Order Already Cancelled")
        session.close()
        return

    # Delivered

    if order.order_status == "Delivered":
        print("Delivered Orders Cannot Be Cancelled.")
        session.close()
        return

    # Pending / Preparing

    if order.order_status in ["Pending", "Preparing"]:
        items = (
            session.query(OrderItems)
            .filter(OrderItems.order_id == order.order_id).all()
        )

        for item in items:
            food = (session.query(Food).filter(Food.food_id == item.food_id).first())
            food.quantity += item.quantity

            if food.quantity > 0:
                food.availability = True

        order.order_status = "Cancelled"

        payment = (
            session.query(Payments)
            .filter(Payments.order_id == order.order_id).first()
        )

        if payment:
            payment.payment_status = "Refund Initiated"

        session.commit()

        print("\nOrder Cancelled Successfully.")
        print("Quantity Restored.")

        if payment:
            print("Refund Initiated.")

        session.close()
        return

    # Out For Delivery

    if order.order_status == "Out For Delivery":
        print("\n" + "=" * 60)
        print("WARNING")
        print("If you cancel now, NO REFUND will be provided.")
        print("=" * 60)
        print("1. Cancel Order")
        print("2. Back")

        choice = get_required_input("Choice: ")

        if choice == "1":
            order.order_status = "Cancelled"
            session.commit()
            print("\nYour Order Is Cancelled.")
            print("No Refund Will Be Provided.")

        else:
            print("Cancellation Aborted.")

    session.close()

# Cancel order closed


# Customer menu section start

def customer_menu(user):

    customer_id = user.customer_id

    while True:
        print("\n" + "=" * 40)
        print("         CUSTOMER MENU")
        print("=" * 40)
        print("1. View Foods")
        print("2. Place Order")
        print("3. View My Orders")
        print("4. Payment")
        print("5. Cancel Order")
        print("6. Logout")

        choice = get_required_input("Enter Choice: ")

        if choice == "1":
            view_foods()

        elif choice == "2":
            place_order(customer_id)

        elif choice == "3":
            view_my_orders(customer_id)

        elif choice == "4":
            payment(customer_id)

        elif choice == "5":
            cancel_order(customer_id)

        elif choice == "6":
            print("Customer Logged Out Successfully.")
            break

        else:
            print("Invalid Choice")
    
# Customer menu closed


# Login or Registration

while True:

    choice = input("\nChoose (Register/Login): ").strip().lower()

    if choice == "register":
        register()

    elif choice == "login":
        user = login()

        if user is None:
            print("Invalid Username / Password / Role")
            continue

        print(f"\nWelcome {user.username}")

        if user.role.lower() == "admin":
            admin_menu()

        else:
            customer_menu(user)

    else:
        print("Please Enter Register or Login.")

# Closed
