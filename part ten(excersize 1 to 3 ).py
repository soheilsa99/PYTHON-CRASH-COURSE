print('practice one: Learning Python')
file_nema = 'learning_python.txt'

with open(file_nema) as file_object:
    content = file_object.read()
    print(content)


# Also we can use pathlib library

from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

#------------------------------------------------------------

with open(file_nema) as file_object:
    for line in file_object:
        print(line.rstrip())

contents = path.read_text().rstrip()
print(contents)


#-------------------------------------------------------------

for line in lines:
    print(line.rstrip())


lines = contents.splitlines()
for line in lines:
    print(line)

print("--------------------------------------------------------")
print('practice two: Learning Python')

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
print("--------------------------------------------------------")
print('practice three: Simpler Code')

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
  print(line)