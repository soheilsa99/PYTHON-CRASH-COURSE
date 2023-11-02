"""
OOP(Object_Oriented Programming) : Use class as blueprint to represent real_world thing
class : Attribute(datta, feature and .... ) , Behavior (using , act and ....)
Instantiation : Creating an object from a class
"""
class Dog:
    """A simple attempt to model a dog."""
    # __init__ method is called automatically when is object created
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")


#Calling Methods
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()


# Creating Multiple Instances
my_dog = Dog("willie", 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age}")
my_dog.sit()

print(f"My dog's name os {my_dog.name}")
print(f"your dog is {your_dog.age} years old.")
your_dog.sit()

"""
method : A function associated with a class
tip : every method needs a parameter "self"
Use dot notation to call methods or attributes on an object
"""

print("-------------------------------------------------------------------------------")
print("Practice one : Restaurant ")


class Restaurant:
    """A simpl restaurant class with 3 method for show restaurant name open and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize cuisine type and restaurant name."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant ."""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        """Describe that restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")


restaurant = Restaurant('Mia', 'Italian')
print(f"Restaurant name: {restaurant.restaurant_name}.")
print(f"Restaurant cuisine: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("-------------------------------------------------------------------------------")
print("Practice two : Three Restaurant ")


class Restaurant:
    """
    A simpl restaurant class with 3 method for show
    restaurant name, open and cuisine type with 3 restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize cuisine type and restaurant name."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant ."""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is: {self.cuisine_type}")

    def open_restaurant(self):
        """Describe that restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")


restaurant_1 = Restaurant('Mia', 'Italian')
restaurant_2 = Restaurant('Sophia', 'French')
restaurant_3 = Restaurant('Golden Dragon', 'Chinese')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("-------------------------------------------------------------------------------")
print("Practice Three : User")


class user:
    def __init__(self, age, id, name, family):
        """Initialize user class with much information attributes. """
        self.age = age
        self.id = id
        self.name = name
        self.family = family

    def describe_user(self):
        """Describe a user"""
        print(f"The user name is {self.name} {self.family}")
        print(f"The user is {self.age} years old")

    def greet_user(self):
        """Greeting to user"""
        print(f"Hi {self.name.title()} {self.family}")


u1 = user(19, 'zizigolo33', 'mohamad', 'kiana')
u1.describe_user()
u1.greet_user()


print("person 2 ------------------------------------------------------------------" )
u2 = user(54, 'zhila', 'Roham', 'Sadeghi')
u2.describe_user()
u2.greet_user()