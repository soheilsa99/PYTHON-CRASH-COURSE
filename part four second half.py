players = ["Jacki", "Billy", "Amely", "luci", "samuel", "gabriel", "micheal"]
# This 3 order is same
print(players[0:3])
print(players[:3])
for player in players[:3]:
    print(player.title())
# This 2 order is same
print(players[2:])
print(players[-5:])
friend = players[:]
# coppy the second list(left side) to first variable (right side)
print(f"\n My friend name is :{friend}")
print("-------------------------------------------------------------------------")
food_me = ["ghorme sabzi", "koko", "flafel", "gheyme"]
friend_food = food_me[:]
friend_food.append("omlet")
print(friend_food)
print("-------------------------------------------------------------------------")
print("practice slices 4_10")
animals = ["bird", "cat", "kangaroo", "tiger", "leopard"]
print("The first three massage item in the list are :")
print(animals[:3])
print(f"The three middle of the list are : {animals[2:5]}")
print("also we can print three middle item with for loop :")
for animal in animals[2:5]:
    print(animal)
print("The last three massage item in the list are :")
for animal in animals[2:]:
    print(animal)
print(f"The three last item of the list are : {animals[2:5]}")
print("-------------------------------------------------------------------------")
print("practice My pizza, Your pizza 4_11 and 4_12")
pizzas = ["special", "chicken", "peperoni", "vegetable"]
my_friend_pizza = pizzas[:]
pizzas.append("margarita")
print(pizzas)
my_friend_pizza.append("meat and mushroom")
print(my_friend_pizza)
print("my favorite pizzas are: ")
for pizza in pizzas[:]:
    print(pizza)
print("my friend favorite pizzas are: ")
for pizza in my_friend_pizza[:]:
    print(pizza)
print("-------------------------------------------------------------------------")
print("Tuples(list item that can not change )")
dimensions = (200, 2)
print(dimensions[0])
print(dimensions[1])
"""
we can't update the  element after we write Tuple
for ex)deimensions[0] = 150
"""
for dimension in dimensions:
    print(dimension)
print("a Tuple with on element should have use a ',' after the element")
my_t = (20,)
print(my_t)
print("-------------------------------------------------------------------------")
for dimension in dimensions:
    print(dimension)
# overwrite a new tuple with same name
print("new value")
dimensions = (300, 39, 49)
for dimension in dimensions:
    print(dimension)
print("-------------------------------------------------------------------------")
simple_food = ("bread and cheese", "pasta", "rice", "oats")
for food in simple_food:
    print(food)
simple_food = ("bread and cheese", "pasta", "rice", "oats" , 'taco shel')
for food in simple_food:
    print(food)