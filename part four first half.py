magicians = ["alic", "david", "carolina"]
"""
The format of for loop is : 
for item in list_of_items:
"""
for magician in magicians:
    print(f"{magician.title()}, that was great trick")
    print(f"I can't wait to see your next trick{magician.title()}.\n")
print("thank you, everyone.That was a magic show")
print("-------------------------------------------------------------------------")
# practice Pizzas  4_1
pizzas = ["special", "chicken", "peperoni", "vegetable"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("I really like chicken pizza ,It has delicious taste")
# in khat bala ra kalamatesh y negah konam shayad eshtebah type kardam maza
print("-------------------------------------------------------------------------")
# practice Animal  4_2
animals = ["bird", "cat", "kangaroo"]
for animal in animals:
    print(animal)
    print(f"{animal.title()} it is funny animal")
print("Any of these animals has special beauty")
print("-------------------------------------------------------------------------")
for value in range(2, 8):
    print(value)


even_number = list(range(0, 43, 2))
print(even_number)
#diffrent way for compute even number between 2 number
print("The even number between 0 and 43 is :")
for i in range(0, 43, 2):
    print(i)
#diffrent way for compute even number between 2 number
even_number = []
for i in range(0, 43, 2):
    even_number.append(i)
print(even_number)
print("-------------------------------------------------------------------------")

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(max(squares))
print(min(squares))
"""
list comprehension : A list comprehension combine the for loop and the
                     creation of new elements into one line and automatically
                     appends each new element
"""
# The comprehension example
squares = [value**2 for value in range(1,11)]
print(squares)
print("-------------------------------------------------------------------------")
# practice Counting to Twenty  4_3
for number in range(1, 21):
    print(number)
print("-------------------------------------------------------------------------")
# one Million  4_4
for number in range(1, 1000001):
    print(number)
print("-------------------------------------------------------------------------")
# one Million  4_5
l = []
for number in range(1, 1000001):
    l.append(number)
print(l)
print(f"the mux number in list is :{max(l)}")
print(f"the min number in list is :{min(l)}")
print(f"the sum of the list is :{sum(l)}")
print("-------------------------------------------------------------------------")
# Odd number  4_6
o_n = list(range(1, 20, 2))
print(o_n)
print("-------------------------------------------------------------------------")
# Threes  4_7
numbers = list(range(3, 31, 3))
for n in numbers:
    print(n)
# start stop step*
# *i+1
print("-------------------------------------------------------------------------")
# Cubes  4_8 and 4_9
cube = [value**3 for value in range(1, 11)]
print(cube)
