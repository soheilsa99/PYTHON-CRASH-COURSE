# """
# function : blocks of code designed to do one specific job
# function has this format:
#
# def name of function(parameter)
# ....
# name of function(argument)
#
# parameter: a piece of information the function need to do this job
# argument : a piece of information that is passes from a function call to function
# """
#
#
# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"hello, {username.title()}!")
#
#
# greet_user('jesse')
# # ------------------------------------------------------------------------------------
# print("Practice one : message")
#
#
# def display_massage(new_learn):
#     print(f"Hello everyone ,{new_learn}")
#
#
# display_massage("I learn to write a simple function ,It's so interesting :)")
#
#
# # also we can write
# def display_massage():
#     print("I learn to write a simple function ,It's so interesting :)")
#
#
# display_massage()
# print("-------------------------------------------------------------------------------")
# print("Practice two : Favorite Book")
#
#
# def favorite_book(title):
#     print(f"One of the my favorite books is {title}")
#
#
# favorite_book(title='The Untethered Soul')
# print("-------------------------------------------------------------------------------")
#
#
# # function has multiple parameter need multiple arguments
# # positional argument
# def describe_pet(animal_type, pet_name):
#     """Display information about pet"""
#     print(f"\n I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
#
#
# describe_pet('hamster', 'harry')
# # we can change the order of passing arguments 'Keyword Argument '
# describe_pet(pet_name='harry', animal_type='hamster')
#
#
# # if we use a hint(PEP484) in our IDE we should follow the order of parameters
# # -------------------------------------------------------------------------------------
#
#
# # Default value example
# def describe_pet(pet_name, animal_type='dog'):
#     # we should use default value at the end
#     """Display information about pet"""
#     print(f"\n I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
#
#
# describe_pet('willie')
#
# print("-------------------------------------------------------------------------------")
# print("Practice three : T-Shirt")
#
#
# # positional argument
# def T_Shirt(text, size):
#     print(f"we need T_Shirt with {size} size and write this text on it : {text}")
#
#
# T_Shirt('I love programing and math', 'Xl')
# T_Shirt('I am junior programmer', 'XXl')
#
#
# # -------------------------------------------------------------------------------------
#
#
# # Keyword argument
# def T_Shirt(text, size):
#     print(f"we need T_Shirt with {size} size and write this text on it : {text}")
#
#
# T_Shirt(text='I love programing and math', size='Xl')
# T_Shirt(text='I am junior programmer', size='XXl')

# print("-------------------------------------------------------------------------------")
# print("Practice four : Large Shirt")
#
#
# # positional argument
# def make_shirt(text, size):
#     print(f"{text} with this {size} size shirt")
#
#
# make_shirt("Enjoy your life", "XXL")
# make_shirt("I love researching", "XL")
# make_shirt("I love Python", "Large")
# make_shirt("I love Python", "Medium")
#
#
# # -------------------------------------------------------------------------------------
# # Keyword argument
# def make_shirt(text, size):
#     print(f"{text} with this {size} size shirt")
#
#
# make_shirt(text="Enjoy your life", size="XXL")
# make_shirt(size="XL", text="I love researching")
# make_shirt(text="I love Python", size="Large")
# make_shirt(size="Medium", text="I love Python")
#
# # -------------------------------------------------------------------------------------
# # default value
# """
# we can't have default value and Keyword argument in one function
# if we use them together we will see incorrect result
# we can have default value and positional argument in one function and have correct result
# """
#
#
# def make_shirt(size, text="I love Python"):
#     print(f"{text} with this {size} size shirt")
#
#
# make_shirt(size="Large")
# make_shirt(size="Medium")
# make_shirt(size="XXL", text="Enjoy your life")
# make_shirt(size="XL", text="I love researching")

print("-------------------------------------------------------------------------------")
print("Practice five : cities")


def describe_city(city, country="Iran"):
    print(f"{city} is in {country}")


describe_city(city="Esfahan")
describe_city(city="Shiraz")
describe_city(city="Yazd")
describe_city(city="Los Angeles", country="USA")


# # ----------------------------------------------------------------------------------
# # example for Return Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jami', 'hendrix')
# print(musician)
# ----------------------------------------------------------------------------------
"""
Making an Argument optional :
sometime we don't now exactly what user want or what information they have.
we use the extra argument , user can send extra information or lower 
"""


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name(first_name='jimi', last_name='hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
