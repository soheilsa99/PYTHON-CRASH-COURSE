"""
we use Pathlib library for read text file
we can do lots of thing with path object that point to file
"""
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
print("__________________________________________________________________________")
# we can remove an extra blanket line in output with using rstrip() on content
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
"""
also we can do it with this format
contents = path.read_text().rstrip()
"""
print(contents)
print("---------------------------------------------------------------------------")
"""
Relative and Absolute File Paths
sometime the files are not in same directory with code 
"""
path = Path("C:/Users/sohei/Downloads/pi_digits.txt")
contents = path.read_text().rstrip()
print(contents)
print("---------------------------------------------------------------------------")
"""
Accessing a File's Lines
some time we need use data from certain line of file
splitlines() method turn a long string of lines and the use a for loop to examine each line from a file
"""
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

