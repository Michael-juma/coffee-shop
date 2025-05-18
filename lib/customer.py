
from order import Order


class Customer:
    # Class variable to keep track of all Customer instances
    all_customers = []

    # Constructor method to create a new Customer
    def __init__(self, name):
        # Set the customer's name using the setter
        self.name = name
        # Add the new customer to the list of all customers
        Customer.all_customers.append(self)

    # Getter for the name attribute
    @property
    def name(self):
        return self._name

    # Setter for the name attribute with validation
    @name.setter
    def name(self, value):
        # Name must be a string between 1 and 15 characters
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError(
                "Customer name must be a string between 1 and 15 characters.")
        self._name = value

    # Method to get all orders made by this customer
    def orders(self):
        # Return a list of orders where this customer matches
        return [order for order in Order.all_orders if order.customer == self]

    # Method to get all unique coffees ordered by this customer
    def coffees(self):
        # Use a set to remove duplicates, then convert to list
        return list(set(order.coffee for order in self.orders()))

    # Method for the customer to create a new order
    def create_order(self, coffee, price):
        # Return a new Order instance linked to this customer
        return Order(self, coffee, price)

    # Class method to find the customer who spent the most on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        # Dictionary to store total spending per customer for the given coffee
        customer_spending = {}

        # Loop through all orders to find relevant ones
        for order in Order.all_orders:
            if order.coffee == coffee:
                # Add the price to the customer's total spending
                customer_spending[order.customer] = customer_spending.get(
                    order.customer, 0) + order.price

        # If no customer has ordered this coffee, return None
        if not customer_spending:
            return None

        # Return the customer who spent the most on this coffee
        return max(customer_spending, key=customer_spending.get)


# Import the Order class at the end to avoid circular import issues
