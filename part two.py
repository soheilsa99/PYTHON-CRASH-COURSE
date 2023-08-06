# 2_1 simple Massage
#We can write string with variable
second_massage = 'Hi guys'
print(second_massage)
# -------------------------------------------------------------
# 2_2
second_massage = 'Hi guys'
print(second_massage)
#update a variable value and use it again
second_massage = "hello my veiwer of github , this is update of variable"
print(second_massage)
# -------------------------------------------------------------
f_name = ' Soheil '
l_name = "Sarami "
print("hello, Soheil Sarami. Nice to meet you. ")
print(f"hello, {f_name.title()} {l_name.title()}, Nice to meet you.")
print(f"hello, {f_name.title().lstrip()} {l_name.title().rstrip()}, Nice to meet you.")
full_name =f"{f_name}{l_name}"
print(f"hello, {full_name.strip()}, Nice to meet you.")
# -------------------------------------------------------------
"""
tip ! when we should use single qutation for correct grammer 
for example
"""
greet = 'hello'
print(f'{greet} ,It\'s warm today ')
print(f"{greet} ,It's warm today ")
# we use a \' or we can use " '   "
# ---------------------------------------------------------------
# 2_3,4
f_name = ' SOHEIL '
l_name = "sarami "
print("hello, Soheil Sarami. Nice to meet you. ")
print(f"Hello, {f_name.title().lstrip()}{l_name.title().rstrip().title()}. Nice to meet you.")
# -------------------------------------------------------------
# 2_5
famouse_person = "Albert Einistein"
famouse_quote = "A person who never made a mistake never tried anything new  "
print(f"\t{famouse_person} once said : \n\t\"{famouse_quote}\"")
# -------------------------------------------------------------
# 2_6
famouse_person = "Albert Einistein"
massage = "A person who never made a mistake never tried anything new  "
print(f"\t{famouse_person} once said : \n\t\"{massage}\"")
# -------------------------------------------------------------
# 2_7
m = " John "
print(m.rstrip())
print(m.lstrip())
print(m.strip())
# -------------------------------------------------------------
# 2_8
wikipedia_url = 'https://en.wikipedia.org/wiki/Programming_language'
without_prefix = wikipedia_url.removeprefix('https://')
print(f"without perfix is : {without_prefix}")
without_suffix = wikipedia_url.removesuffix('/wiki/Programming_language')
print(f"without_suffix is : {without_suffix}")
# -------------------------------------------------------------
# 2_9
# Perform the four basic operations of mathematics on two numbers
print(6+1)
print(6/7)
print(6*4)
print(6-3)
# -------------------------------------------------------------
favorite_number = 72
print(f"My favorite number is : {favorite_number}")