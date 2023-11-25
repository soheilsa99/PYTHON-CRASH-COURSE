"""
We can save data by write it in file ...
Writing a Single Line :
we have path defined  we can write to a file by using 'write_text()' method
"""

from pathlib import Path
path = Path("programing.txt")

path.write_text("I love programming.")
contents = path.read_text()
print(contents)


"""
Tip ! python can only write string to a text file. If we want to store numerical data
in a text file , we'll have to convert the data string format first using the str() function
"""

# Write Multiple Lines
from pathlib import Path
"""
Tip ! Don't add many line directly in file, We should use variable to save line ;
 after we can write_text(variable_name)
"""

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data. \n"

path = Path('programing.txt')
path.write_text(contents)
print(contents)