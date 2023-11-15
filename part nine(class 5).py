# # The Python Standard Library
# from random import randint
# print(randint(3, 9))
# print(randint(4, 12,))

# print("----------------------------------------------------------------------")
# print("Practice thirteen : Dice")
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll_die(self):
#         print(randint(1, self.sides))
#
# die = Die(6)
# for _ in range(0, 10):
#     die.roll_die()


print("----------------------------------------------------------------------")
print("Practice fourteen : Lottery")

from random import choice
values = [67, 77, 44, 32, 29, 23, 34, 43, 221, 221, 'z', 'v', 's', 'a']

print("The following tickets have won a prize")
for _ in range(0, 4):
    print(choice(values))

print("----------------------------------------------------------------------")
print("Practice fifteen : Lottery Analysis")

from random import choice
values = [67, 77, 44, 32, 29, 23, 34, 43, 221, 221, 'z', 'v', 's', 'a']

my_ticket = choice(values)

for i in range(0, len(values)):
    print(choice(values))
    if values[i] == my_ticket:
        print(f"It took {i+1} iterations to get the ticket {values[i]}")
        break