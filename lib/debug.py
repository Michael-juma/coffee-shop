from customer import Customer
from coffee import Coffee

alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.0)
bob.create_order(latte, 5.0)
alice.create_order(latte, 4.0)
bob.create_order(espresso, 6.0)

print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)
