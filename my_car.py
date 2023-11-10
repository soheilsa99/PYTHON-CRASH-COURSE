print("Importing Single class")
from car1 import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("----------------------------------------------------------------------")
print("Storing Multiple Class in a module")

from car2 import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("----------------------------------------------------------------------")
print("Importing Multiple Class from Module")

from car2 import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('niessan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print("----------------------------------------------------------------------")
print("Importing an Entire Module")

import car2
my_mustang = car2.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print("----------------------------------------------------------------------")
print("Importing All Classes from a Module")
# Format : from module_name import *
"""
If you need to import many classes from a module, you're better of importing 
the entire module and using the module_name.ClassName syntax.
You won't see all the classes used at the top of the file, but you'll see clearly 
where the module is used in the program . You will also avoid the potential naming
conflicts that can arise when you import every class in a module. 
"""


print("----------------------------------------------------------------------")
print("Importing a Module into a Module")

from car1 import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

print("----------------------------------------------------------------------")
print("Using Aliases")

from electric_car import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
