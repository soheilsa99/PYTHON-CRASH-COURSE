class Car:
    """A simpl attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

#--------------------------------------------------------------------------------------------------------


"""
Inheritance : sometime class that we write(child class) is version of the another class(parent class)
take an attributes and method from the first class
"""

# The __init__() Method for a Child Class
#exampl for inheritance
# Class child_name(parent_name):
class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

"""
Tip ! the parent class should define in same file with child class , also we must define a child class
after parent class

Tip ! super() function is special function that allows you to call a method from the parent class.
child class = subclass
parent class = superclass
"""


"""
Defining Attributes and Methods for the Child Class
Sometime we need to change the child class (a new attribute that parent class don't have)
"""
class Car:
    """A simpl attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
#exampl for inheritance
# Class child_name(parent_name):
class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize  attributes of  the parent class
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


#Overriding Methods from the parent Class
"""
we can override any method from parent class to suit for child class target
"""
# Instance as Attributes
class Car:
    """A simpl attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}kwh battery")

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize  attributes of  the parent class
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

#--------------------------------------------------------------------------------------------------------
#Add another method of battery for report range of the car based on the battery size
class Car:
    """A simpl attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}kwh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize  attributes of  the parent class
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("-------------------------------------------------------------------------------")
print("Practice six : Ice Cream Stand")
# I use the code of practice four
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


class IceCreamStand(Restaurant):
    """A simple ice cream class stand with class Restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavor(self):
        """Display ice cream flavor"""
        print(f"the flavor are:")
        for flavor in self.flavors:
            print(f"- {flavor}")

i_cream = IceCreamStand("Marof" , 'ice cream', ['caramel', 'blueberry', 'chocolate'])
i_cream.display_flavor()

print("-------------------------------------------------------------------------------")
print("Practice seven : Admin")
# I use the code of practice five


class User:
    def __init__(self, age, id, name, family):
        """Initialize user class with much information attributes. """
        self.age = age
        self.id = id
        self.name = name
        self.family = family
        self.login_attempts = 0

    def describe_user(self):
        """Describe a user"""
        print(f"The user name is {self.name} {self.family}")
        print(f"The user is {self.age} years old")

    def greet_user(self):
        """Greeting to user"""
        print(f"Hi {self.name.title()} {self.family}")

    def increment_login_attempts(self):
        """Increments number of login attempts by one"""
        self.login_attempts += 1

    def rest_login_attempts(self):
        """Resets number of login attempts to zero"""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, age, id, name, family, privileges):
        super().__init__(age, id, name, family)
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges"""
        print("privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('Soheil',  'Admin', 'nbc', 21, ['can add post', 'can delete post', 'can be user'])
admin.show_privileges()