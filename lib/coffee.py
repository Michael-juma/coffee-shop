
from order import Order

class Coffee:
    # Class variable to store all instances of Coffee
    all_coffees = []

    # Constructor method to initialize a new Coffee instance
    def __init__(self, name):
        # Set the name attribute using the setter
        self.name = name
        # Add the new coffee instance to the class-level list
        Coffee.all_coffees.append(self)

    # Getter for the name attribute
    @property
    def name(self):
        return self._name

    # Setter for the name attribute with validation
    @name.setter
    def name(self, value):
        # Ensure the name is a string with at least 3 characters
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError(
                "Coffee name must be a string with at least 3 characters.")
        self._name = value

    # Method to return all orders associated with this coffee
    def orders(self):
        # Filter all orders to only those where the coffee matches this instance
        return [order for order in Order.all_orders if order.coffee == self]

    # Method to return all unique customers who ordered this coffee
    def customers(self):
        # Use a set to remove duplicates, then convert to a list
        return list(set(order.customer for order in self.orders()))

    # Method to count how many orders exist for this coffee
    def num_orders(self):
        return len(self.orders())

    # Method to calculate the average price of orders for this coffee
    def average_price(self):
        # Extract prices from all orders for this coffee
        prices = [order.price for order in self.orders()]
        # Return the average if there are prices, otherwise return 0
        return sum(prices) / len(prices) if prices else 0
