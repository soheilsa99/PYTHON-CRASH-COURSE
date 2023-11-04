print("working with a class and instances")
print("Example : The Car Class")
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

#----------------------------------------------------------------------------------------------------------------
print("Setting a Default Value for an Attribute")

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#----------------------------------------------------------------------------------------------------------------
print("Modifying Attribute Values")
# this ex : modifying attribute's value DIRECTLY


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("Modifying an Attribute's Value Through a Method")
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 234
my_new_car.read_odometer()

print("Incrementing an Attribute's Value Through a Method")
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()

    def read_odometer(self):
        """Print statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.increment_odometer(-500)
my_used_car.read_odometer()

print("-------------------------------------------------------------------------------")
print("Practice four : Number Served ")

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


restaurant = Restaurant('Sophia', 'French')
restaurant.describe_restaurant()
print(f"Number of served: {restaurant.number_served}")

restaurant.number_served = 200
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(300)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(700)
print(f"Number served: {restaurant.number_served}")


print("-------------------------------------------------------------------------------")
print("Practice five : User")


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


u1 = User(19, 'zizigolo33', 'mohamad', 'kiana')
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"Login attempts: {u1.login_attempts}")

u1.rest_login_attempts()
print(f"login attempts (after reset): {u1.login_attempts}")
