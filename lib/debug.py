from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
c1 = Customer("Alice")
c2 = Customer("Bob")
c3 = Customer("Charlie")
c4 = Customer("Diana")

cof1 = Coffee("Espresso")
cof2 = Coffee("Latte")
cof3 = Coffee("Cappuccino")
cof4 = Coffee("Latte")

# Valid Order
try:
    o1 = Order(c1, cof1, 4.5)
    o2 = Order(c2, cof2, 9.0)
    o3 = Order(c3, cof3, 7.5)
    o4 = Order(c4, cof4, 8.2)
    print(" Valid orders created.")
except Exception as e:
    print("Error creating valid order:", e)

# Invalid customer
try:
    o3 = Order("NotCustomer", cof1, 3.0)
except Exception as e:
    print(" Correctly failed with invalid customer:", e)

# Invalid coffee
try:
    o4 = Order(c1, "NotCoffee", 3.0)
except Exception as e:
    print("Correctly failed with invalid coffee:", e)

# Invalid price (too low)
try:
    o5 = Order(c1, cof1, 0.5)
except Exception as e:
    print("Correctly failed with invalid price (low):", e)

# Invalid price (not float)
try:
    o6 = Order(c1, cof1, "not a float")
except Exception as e:
    print("Correctly failed with non-float price:", e)

# Show all orders
print("All orders:", Order.all_orders)
