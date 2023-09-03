cars = ["Toyota", "bmw", "subaro", "audi"]
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("--------------------------------------------------------------------------------------------------------------")
car = 'benz'
# we can compare the variable
print(car == "audi")
car2 = "subaro"
# != a sign for inequality , not same
if car2 != 'benz':
    print('you want bad choice')
print("--------------------------------------------------------------------------------------------------------------")
password = 123
if password != 234:
    print("it is an incorrect password")
print("--------------------------------------------------------------------------------------------------------------")
age = 23
print(age > 18)
print(22 <= age)
# we can check with 2 state
print((age > 18) or (22 <= age))
print("--------------------------------------------------------------------------------------------------------------")
user = 453
Pass = 123
# we can check with 2 state
if((user == 453) and (Pass == 123)):
    print("it is ok")
print((user == 453) and (Pass == 123))
print("--------------------------------------------------------------------------------------------------------------")
requested_toppings = ["mushroom", "onion", "pineapple"]
# we can chek the is it exist in list?
print("potato" in requested_toppings)
print("mushroom" not in requested_toppings)
print('tomato' in requested_toppings)
print("--------------------------------------------------------------------------------------------------------------")
banned_users = ["sam", "jack", "andrew", "david"]
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")
else:
    print("you can't ")
user = "sam"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")
else:
    print(f"{user.title()} you can't ")
print("--------------------------------------------------------------------------------------------------------------")
print("Practice 5_1 Conditional Tests")
nationality = "Russian"
print(" Is your nationality == 'Iranian' ? I predict False.")
print(nationality == 'Iranian')
print(" Is your nationality == 'Russian' ? I predict True.")
print(nationality == 'Russian')
nationality = "Italian"
print(" Is your nationality == 'Italian' ? I predict True.")
print(nationality == 'Italian')
print(" Is your nationality == 'Russian' ? I predict False.")
print(nationality == 'Russian')
print(" Is your nationality == 'English' ? I predict False.")
print(nationality == 'English')
print(" Is your nationality == 'British' ? I predict False.")
print(nationality == 'British')
nationality = "Spanish"
print(" Is your nationality == 'spanish' ? I predict True.")
print(nationality == 'Spanish')
nationality = "Vietnamese"
print(" Is your nationality == 'vietnamese' ? I predict True.")
print(nationality == 'Vietnamese')
print("--------------------------------------------------------------------------------------------------------------")
car = 'Audi'
print(car.lower() == 'audi')
print("--------------------------------------------------------------------------------------------------------------")
age = 23
if age < 6 :
    print("your admission cos is $0")
elif age < 14:
    print("your admission cos is $25")
else :
    print("your admission cos is $45")
#We can do it with another way for example
age = 5
if age < 6 :
     c_admission = 0
elif age <= 14:
     c_admission = 25
else :
     c_admission = 45
print(f"your admission cost is ${c_admission}")
print("--------------------------------------------------------------------------------------------------------------")
requested_toppings = ["mushroom", "peperoni", "extra cheese"]
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'extra pepper' in requested_toppings:
    print("extra pepper")
print("you make special pizza that you want")
print("--------------------------------------------------------------------------------------------------------------")
print("Practice 5_3 Alien Color")
color = "yellow"
if color == "yellow" :
    print("your gues is correct ,You earn 5 point ")
color = "blue"
if color == "yellow" :
    print("your gues is correct ,You earn 5 point ")
print("--------------------------------------------------------------------------------------------------------------")
print("Practice 5_4 Alien Color#2")
color = "green"
if color == "green" :
    print("You earn 5 point ")
else:
    print("just earned 10 points ")
print("--------------------------------------------------------------------------------------------------------------")
print("Practice 5_4 Alien Color#3")
color = "green"
if color == "green" :
    print("You earn 5 point ")
if color == "yellow":
    print("just earned 10 points")
if color == "red":
    print("just earned 15 points ")
# check yellow
color = "yellow"
if color == "green" :
    print("You earn 5 point ")
if color == "yellow":
    print("just earned 10 points")
if color == "red":
    print("just earned 15 points ")
# check red
color = "red"
if color == "green" :
    print("You earn 5 point ")
if color == "yellow":
    print("just earned 10 points")
if color == "red":
    print("just earned 15 points ")