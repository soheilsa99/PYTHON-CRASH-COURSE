m = input("Tell me something ,It back to you :")
print(m)
# ---------------------------------------------------
name = input("pleas enter your name :")
print(f"\n Hello, {name}!")
# also we can say
name = "pleas enter your name ,"
name += "I will send you greeting massage :"
i=input(name)
print(f"hi {i},welcome")
# ---------------------------------------------------
age = int(input("How old are you?"))
# ---------------------------------------------------
height = int(input("How tall are you, in centimeter"))
if height >= 148:
    print("\n You're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're little older")
print("------------------------------------------------------")
"""
 we can check the number is even or odd
"""
print(3 % 2)
print(6 % 3)
print(4 % 2)
print("------------------------------------------------------")
number = int(input("Enter a number, and I will tell you if it's even or odd:"))
if number % 2 == 0:
    print(f"\n The number {number} is even")
else:
    print(f"\n The number {number} is odd")
print("------------------------------------------------------")
print("practice one : Rental Car")
t_car = input("what kind of car would you like ?")
print(f"You want a {t_car}, let me see if i can find a Subaru ")
print("------------------------------------------------------")
print("practice two : Restaurant Seating")
number = int(input("How many people  are in your dinner group"))
if number < 0:
    print("You write an invalid number of people")
elif number < 8:
    print("Your table is ready :)")
else:
    print("please waite for table")
print("------------------------------------------------------")
print("practice three : Multiples of Ten")
n = int(input("please enter number ,I will say you ;Is it multiple of ten"))
if n % 10 == 0 :
    print("Number is multiple of 10 ")
else:
    print('It is not multiple')
print("------------------------------------------------------")
current_number = 1
while current_number <= 5:
    print(current_number)
#     current_number +=1
print("------------------------------------------------------")
prompt = "\n Tell me something, and I will repeat it back to you "
prompt += "\n Enter 'quit' to end the program"
message = ''

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# We can also make that program with flag statement
prompt = "\n Tell me something, and I will repeat it back to you "
prompt += "\n Enter 'quit' to end the program"
message = ''
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
print("------------------------------------------------------")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("------------------------------------------------------")
x = 1
while x <= 5:
    print(x)
    x += 1
# This loop is forever
# x = 1
# while x <= 5:
#   print(x)