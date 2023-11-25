# print('practice four: Guest')
# from pathlib import Path
# path = Path('guest.txt')
#
# f_name = input("pleas enter your name :")
# path.write_text(f_name.title())

print("---------------------------------------------------------")
print('practice five: Guest Book')

from pathlib import Path
path = Path('Guest_Book.txt')

prompt = "\n please enter your name :"
prompt += "\nplease Enter 'quit' if you're the last guest."
guests = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guests.append(name)
file_string = ''
for name in guests:
    file_string += f"{name}\n"

path.write_text(file_string)