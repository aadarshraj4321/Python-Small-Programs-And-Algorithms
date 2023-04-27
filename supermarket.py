# Supermarket Billing System in Python

# Define the Product class
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Define the User class
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Define the Order class
class Order:
    def __init__(self, user, product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity

# Define the Supermarket class
class Supermarket:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, id, name):
        user = User(id, name)
        self.users.append(user)

    def add_product(self, id, name, price):
        product = Product(id, name, price)
        self.products.append(product)

    def add_order(self, user_id, product_id, quantity):
        user = None
        product = None
        for u in self.users:
            if u.id == user_id:
                user = u
                break
        for p in self.products:
            if p.id == product_id:
                product = p
                break
        if user is not None and product is not None:
            order = Order(user, product, quantity)
            self.orders.append(order)

    def view_orders(self):
        total_amount = 0
        for order in self.orders:
            print(f"{order.user.name} ordered {order.quantity} {order.product.name}(s) for {order.product.price * order.quantity} dollars.")
            total_amount += order.product.price * order.quantity
        print(f"Total Amount: {total_amount} dollars.")

# Create an instance of the Supermarket class
supermarket = Supermarket()

# Add users to the supermarket
supermarket.add_user(1, "John")
supermarket.add_user(2, "Jane")

# Add products to the supermarket
supermarket.add_product(1, "Apple", 0.5)
supermarket.add_product(2, "Banana", 0.25)
supermarket.add_product(3, "Orange", 0.75)

# Add orders to the supermarket
supermarket.add_order(1, 1, 2)
supermarket.add_order(2, 2, 5)
supermarket.add_order(1, 3, 1)

# View the orders in the supermarket
supermarket.view_orders()
