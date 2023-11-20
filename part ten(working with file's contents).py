"""
Working with a File's Content after read content of file from memory
"""
from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# print(pi_string)
# print(len(pi_string))

# """
# Large Files: One Million Digits
# python has no inherent limit to how much data we can work with (but system and memory must handle it )
# """
# path = Path('pi_million_digits.txt')
# contents = path.read_text()
#
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
#
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

print("__________________________________________________________________________")
print("Is Your Birthday contained in Pi?")

path = Path('C:/Users/sohei/PycharmProjects/PYTHON-CRASH-COURSE/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("enter your birthday ,in the for of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appear in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")
