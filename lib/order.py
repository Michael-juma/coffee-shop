
class Order:
    # Class variable to store all instances of Order
    all_orders = []

    # Constructor method to initialize a new Order instance
    def __init__(self, customer, coffee, price):
        # Set the customer attribute using the setter
        self.customer = customer
        # Set the coffee attribute using the setter
        self.coffee = coffee
        # Set the price attribute using the setter
        self.price = price
        # Add the newly created order to the class-level list of all orders
        Order.all_orders.append(self)

    # Getter method for the customer attribute
    @property
    def customer(self):
        return self._customer

    # Setter method for the customer attribute with validation
    @customer.setter
    def customer(self, value):
        # Import the Customer class to check instance type
        from customer import Customer
        # Raise error if value is not an instance of Customer
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer")
        # Set the private _customer attribute
        self._customer = value

    # Getter method for the coffee attribute
    @property
    def coffee(self):
        return self._coffee

    # Setter method for the coffee attribute with validation
    @coffee.setter
    def coffee(self, value):
        # Import the Coffee class to check instance type
        from coffee import Coffee
        # Raise error if value is not an instance of Coffee
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        # Set the private _coffee attribute
        self._coffee = value

    # Getter method for the price attribute
    @property
    def price(self):
        return self._price

    # Setter method for the price attribute with validation
    @price.setter
    def price(self, value):
        # Check if the price is a float and within the allowed range
        if not isinstance(value, float) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        # Set the private _price attribute
        self._price = value


    def __repr__(self):
        return f"Order(Customer: {self.customer.name}, Coffee: {self.coffee.name}, Price: {self.price})"
