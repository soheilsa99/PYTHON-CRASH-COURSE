print("practice four : Pizza Topping")
prompt = " What do you want to add in your pizza "
prompt += "(Type 'quiet' to stop adding toppings) : "
while True:
    message = input(prompt)
    print(f"you will add {message} in your pizza")
    if message == 'quit':
        print("you close the menu, Have a good time")

print("------------------------------------------------------")

print("practice five : Movie Tickets")
massage = "please enter your age, I will say how much you should pay : "
while True:
    age = input(massage)
    if age == 'quit':
        print("have a good time :)")
        break
    else:
        age = int(age)
        if age < 3 :
            p = 0
        elif age < 12 :
            p = 10
        else :
            p = 15
        print(f"The price is : {p}$")
        print("you can write a 'quit' and the program will finished")

print("------------------------------------------------------")

print("practice six")
print("Pizza Topping new version")
prompt = " What do you want to add in your pizza "
prompt += "(Type 'quiet' to stop adding toppings) : "
activ = True
while active:
    if activ == False:
        print("you close the menu, Have a good time")
    message = input(prompt)
    print(f"you will add {message} in your pizza")

# --------------------------------------------------------------------------

print(" Movie Tickets new version")
massage = "please enter your age, I will say how much you should pay : "
active = True
while active:
    age = input(massage)
    if age == 'quit':
        print("have a good time :)")
        active = False
    else:
        age = int(age)
        if age < 3 :
            p = 0
        elif age < 12 :
            p = 10
        else :
            p = 15
        print(f"The price is : {p}$")
        print("you can write a 'quit' and the program will finish")

print("------------------------------------------------------")

print("practice seven : infinity (This loop is forever )")
x = 1
while x <= 5:
  print(x)

print("------------------------------------------------------")

unconfirmed_users = ['alic', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user : {current_user.title()}")
    confirmed_users.append(current_user)

print("\n The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# --------------------------------------------------------------------------

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# --------------------------------------------------------------------------

responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your name :")
    response = input("which mountain would you like to climb someday ?")

    responses[name] = response

    repeat = input("would you like to let another person respond ? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n ----- poling result -----------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")


print("------------------------------------------------------")

print("practice eight : Deli")
sandwich_orders = ['Egg', 'Roast_Bef', 'Grilled_Cheese', 'Ham', 'Nutella', 'Grilled_Chicken']
finished_sandwiches = []
for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} Sandwich")
    finished_sandwiches.append(sandwich_order)

print("---------- Finished Sandwich ----------")
for sandwich in finished_sandwiches:
    print(f"We made a {sandwich} sandwich")

print("------------------------------------------------------")

print("practice nine : No Pastrami")
sandwich_orders = ['Egg', 'Pastrami', 'Roast_Bef', 'Grilled_Cheese', 'Pastrami', 'Ham', 'Nutella', 'Grilled_Chicken', 'Pastrami']
finished_sandwich = []
print("Deli has run out Pastrami :(")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    finished_sandwich.append(sandwich_orders)
print("---------- Finished Sandwich ----------")
for i in sandwich_orders:
    print(f"We made a {i} sandwich")

print("------------------------------------------------------")

print("practice ten : Dream Vacation")
responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your name :")
    response = input("If you could visit one place in world, where would you go?")

    responses[name] = response

    repeat = input("would you like to let another person respond ? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n ----- poling result -----------")
for name, response in responses.items():
    print(f"{name} would like to visit {response}")
