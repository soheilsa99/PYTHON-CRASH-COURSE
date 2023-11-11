#Practice ten : Imported_restaurant
class Restaurant:
    """A simpl restaurant class with 3 method for show restaurant name open and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize cuisine type and restaurant name."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant ."""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        """Describe that restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, guests):
        """Set the number of served"""
        self.number_served = guests

    def increment_number_served(self, increment):
        """Add a given number to the number of served guests"""
        self.number_served += increment