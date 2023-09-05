print("practice 5-6 Stage of Life")
age = 45
if (age > 0) and (age < 2):
    print("The person is baby")
elif (age == 2) or age < 4:
    print("Person is toddler")
elif (age == 4) or age < 13:
    print("Person is kid")
elif (age == 13) or age < 20:
    print("The person is teenager")
elif (age == 20) or age < 65:
    print("The person is adult")
elif 65 <= age <= 120:
    print("The person is elder")
else:
    print("You write invalid age")
print("--------------------------------------------------------------------------------------------------------------")
print("practice 5-7 Favorite Fruit")
favorite_fruit = ["Apple", "pineapple", "Orange"]
if "Apple" in favorite_fruit:
    print("you have a good choice")
if "pineapple" in favorite_fruit:
    print("you have a good choice")
if "orange" in favorite_fruit:
    print("you have a good choice")
elif "banana"not in favorite_fruit:
    print("The Bennana is good , test it")
if "kiwi" not in favorite_fruit:
    print("test  common baby ")
print("--------------------------------------------------------------------------------------------------------------")
requested_toppings = ["mushroom", "sauce", "green pepper"]
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry , we sre out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\n Finished making your pizza!")
print("--------------------------------------------------------------------------------------------------------------")
available_toppings = ["mushrooms", "extra cheese", "pepperoni", "olives", "green pepper"]
requested_toppings = ["red pepper", "mushrooms", "peperoni"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza :)")
print("--------------------------------------------------------------------------------------------------------------")
print("practice 5-8 Hello Admin")
usernames = ["sam", "jacki", "gabriel", "admin", "gorge"]
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")
print("--------------------------------------------------------------------------------------------------------------")
print("practice 5-9 No User")
usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")
else:
    print("we need to find some users!")
print("--------------------------------------------------------------------------------------------------------------")
print("practice 5-10 Checking Username")
current_users = ["sam", "jacki", "gabriel", "david", "gorge"]
new_users = ["Gabriel", "david", "sara", "samuel"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Hi {new_user.title()} The username is already in use, please use a different one.")
    else:
        print(f"Hi {new_user.title()}This username is available")
print("--------------------------------------------------------------------------------------------------------------")
print("practice 5-11 Ordinal Numbers")
numbers = list(range(1, 10))
print(numbers)
for number in numbers:
    print(number)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2st")
    elif number == 3:
        print("3st")
    elif number == 4:
        print("4st")
    elif number == 5:
        print("5st")
    elif number == 6:
        print("6st")
    elif number == 7:
        print("7st")
    elif number == 8:
        print("8st")
    else :
        print("9st")
print("practice 5-12 Ordinal Numbers")
print("In last practice we use rules of code style :)")

