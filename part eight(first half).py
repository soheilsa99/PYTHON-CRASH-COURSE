"""
function : blocks of code designed to do one specific job
function has this format:

def name of function(parameter):
....
....
name of function(argument)

parameter: a piece of information the function need to do this job
argument : a piece of information that is passes from a function call to function
"""


def greet_user(username):
    """Display a simple greeting"""
    print(f"hello, {username.title()}!")


greet_user('jesse')
# ------------------------------------------------------------------------------------
print("Practice one : message")


def display_massage(new_learn):
    print(f"Hello everyone ,{new_learn}")


display_massage("I learn to write a simple function ,It's so interesting :)")


# also we can write
def display_massage():
    print("I learn to write a simple function ,It's so interesting :)")


display_massage()
print("-------------------------------------------------------------------------------")
print("Practice two : Favorite Book")


def favorite_book(title):
    print(f"One of the my favorite books is {title}")


favorite_book(title='The Untethered Soul')
print("-------------------------------------------------------------------------------")


# function has multiple parameter need multiple arguments
# positional argument
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
# we can change the order of passing arguments 'Keyword Argument '
describe_pet(pet_name='harry', animal_type='hamster')


# if we use a hint(PEP484) in our IDE we should follow the order of parameters
# -------------------------------------------------------------------------------------


# Default value example
def describe_pet(pet_name, animal_type='dog'):
    # we should use default value at the end
    """Display information about pet"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('willie')

print("-------------------------------------------------------------------------------")
print("Practice three : T-Shirt")


# positional argument
def T_Shirt(text, size):
    print(f"we need T_Shirt with {size} size and write this text on it : {text}")


T_Shirt('I love programing and math', 'Xl')
T_Shirt('I am junior programmer', 'XXl')


# -------------------------------------------------------------------------------------


# Keyword argument
def T_Shirt(text, size):
    print(f"we need T_Shirt with {size} size and write this text on it : {text}")


T_Shirt(text='I love programing and math', size='Xl')
T_Shirt(text='I am junior programmer', size='XXl')

print("-------------------------------------------------------------------------------")
print("Practice four : Large Shirt")


# positional argument
def make_shirt(text, size):
    print(f"{text} with this {size} size shirt")


make_shirt("Enjoy your life", "XXL")
make_shirt("I love researching", "XL")
make_shirt("I love Python", "Large")
make_shirt("I love Python", "Medium")


# -------------------------------------------------------------------------------------
# Keyword argument
def make_shirt(text, size):
    print(f"{text} with this {size} size shirt")


make_shirt(text="Enjoy your life", size="XXL")
make_shirt(size="XL", text="I love researching")
make_shirt(text="I love Python", size="Large")
make_shirt(size="Medium", text="I love Python")

# -------------------------------------------------------------------------------------
# default value
"""
we can have default value and Keyword argument in one function
"""


def make_shirt(size, text="I love Python"):
    print(f"{text} with this {size} size shirt")


make_shirt(size="Large")
make_shirt(size="Medium")
make_shirt(size="XXL", text="Enjoy your life")
make_shirt(size="XL", text="I love researching")

print("-------------------------------------------------------------------------------")
print("Practice five : cities")


def describe_city(city, country="Iran"):
    print(f"{city} is in {country}")


describe_city(city="Esfahan")
describe_city(city="Shiraz")
describe_city(city="Yazd")
describe_city(city="Los Angeles", country="USA")


# ----------------------------------------------------------------------------------
# example for Return Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jami', 'hendrix')
print(musician)
# ----------------------------------------------------------------------------------
"""
Making an Argument optional :
sometime we don't know exactly what user want or what information they have.
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
# ----------------------------------------------------------------------------------
"""
Returning a Dictionary
a function can return any kind of value you nees it
"""


def build_person(f_name, l_name):
    """return a dictionary of information about a person"""
    person = {'first': f_name, 'last': l_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
# ----------------------------------------------------------------------------------
"""
Returning a Dictionary
a function can return any kind of value you nees it
"""


def build_person(f_name, l_name, age=None):
    """return a dictionary of information about a person"""
    person = {'first': f_name, 'last': l_name}
    if age:
        person['age'] = age
    return person


# age is optional parameter


musician = build_person('jimi', 'hendrix', age=23)
print(musician)
# ----------------------------------------------------------------------------------
"""
using a function with a while loop
"""


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name}{last_name}"
    return full_name.title()


while True:
    print("\n please tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("last name")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\n Hello, {formatted_name}!")
print("-------------------------------------------------------------------------------")
print("Practice six : city names")


def city_country(city, country):
    massage = {'City': city, 'Country': country}
    return massage


c1 = city_country('Esfahan', 'Iran')
print(c1)
c2 = city_country('LA', 'USA')
print(c2)
c3 = city_country('New York', 'USA')
print(c3)


# ----------------------------------------------------------------------------------
# also we can say
def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country('Esfahan', 'Iran'))
print(city_country('LA', 'USA'))
print(city_country('New York', 'USA'))
print("-------------------------------------------------------------------------------")
print("Practice seven : Album")


def make_album(artist_name, album_title, songs=None):
    massage = {'artist_name' : artist_name, 'album_title' : album_title, 'songs' : songs}
    return massage


# a1 = make_album('Michael Jackson', 'Thriller')
# print(a1)
# a2 = make_album('yanni', 'Tribute')
# print(a2)
# a3 = make_album('Yanni', 'In My Time')
# print(a3)
# the better solution is don't write a new variable

print(make_album('Michael Jackson', 'Thriller'))
print(make_album('yanni', 'Tribute', 14))
print(make_album('Yanni', 'In My Time'))


print("-------------------------------------------------------------------------------")
print("Practice eight : User Albums")


def make_album(artist_name, album_title, songs=None):
    massage = {'artist_name' : artist_name, 'album_title' : album_title, 'songs' : songs}
    return massage


while True:
    print("\n please tell me your favorite artist and album information:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if artist_name == 'q':
        break

    songs = input("How many song in this album exist : ")
    if artist_name == 'q':
        break
print("-------------------------------------------------------------------------------")
def greet_users(names):
    """Print a simple greeting to each user in list"""
    for name in names:
        msg = f"Hi, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# ----------------------------------------------------------------------------
unprinted_designs = ['phon case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\n The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#modifying(change) a list in function
#we use the function for write same program ad this program


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the model that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phon case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

"""
all function have specific job; for example in last example first function was
handle printing the designs and the second summarize the prints that have been made
use the copy of the list with this format:
list_name[:]
also we can prevent a function from modifying a list by copy the list with
"""


print("-------------------------------------------------------------------------------")
print("Practice nine : Message")


def show_messages(l_parameters):
    print("some interesting things about me :)")
    for l_parameter in l_parameters:
        print(l_parameter)


l_parameters = ['My hobby is reding book', 'I hate to wake up so late', 'I have one nephew']
show_messages(l_parameters)


print("-------------------------------------------------------------------------------")
print("Practice ten : Sending Message ")


def show_messages(l_parameters):
    """print text massage"""
    print("some interesting things about me :)")
    for l_parameter in l_parameters:
        print(l_parameter)

def send_massage(l_parameters, sent_massages):
    """print massage and move to list"""


    while l_parameters:
        l_parameter = l_parameters.pop()
        print(l_parameter)
        sent_massages.append(l_parameter)


l_parameters = ['My hobby is reding book', 'I hate to wake up so late', 'I have one nephew']
sent_massages = []
show_messages(l_parameters)
send_massage(l_parameters, sent_massages)
print(f"first list is {l_parameters} now")
print(f"The second list was coppy the first list : {sent_massages}")


print("-------------------------------------------------------------------------------")
print("Practice eleven : Archived Messages ")


def show_messages(l_parameters):
    """print text massage"""
    print("some interesting things about me :)")
    for l_parameter in l_parameters:
        print(l_parameter)

def send_massage(l_parameters, sent_massages):
    """print massage and move to list"""


    while l_parameters:
        l_parameter = l_parameters.pop()
        print(l_parameter)
        sent_massages.append(l_parameter)


l_parameters = ['My hobby is reding book', 'I hate to wake up so late', 'I have one nephew']
sent_massages = []
show_messages(l_parameters)
# we get coppy from first list and print original list
send_massage(l_parameters[:], sent_massages)
print(f"first list is {l_parameters} now")
print(f"The second list was coppy the first list : {sent_massages}")

# ------------------------------------------------------------------------
"""
" passing an Arbitrary Number og Arguments "
some time we don't know how many argument (just string type) a function need to accept
"""


def make_pizza(*toppings):
    #python with this format parameter (*parameter name) assign to make one tuple
    """Summarize the pizza we are about to make."""
    print("\n Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ----------------------------------------------------------------------------------
"""
" Mixing Positional and Arbitrary Argument "
some time we don't know how many (several type of) argument  a function need to accept
"""


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\n Making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ----------------------------------------------------------------------------------

"""
using Arbitrary Keyword Arguments
function will accept many key and value pair
ex)building user profile , we don't know what kind of information will get
"""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)
print("-------------------------------------------------------------------------------")
print("Practice twelve : Sending Message ")


def menu(*items):
    """print a summary the sandwich ingredients: """
    print("our item for sandwich :")
    for item in items:
        print(f" {item}")

menu()
menu('extra peper', 'salad', 'potato')
menu('red onion', 'mushroom')

print("-------------------------------------------------------------------------------")
print("Practice thirteen  : User Profile ")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Soheil', 'Sarrami',
                              field='Computer Science',
                              location='Iran',
                              hobby='riding a bike')
print(user_profile)


print("-------------------------------------------------------------------------------")
print("Practice fourteen  : Cars ")

def buy(**extera):
    # extera["Manufacture"] = Manufacture
    # extera["Model"] = Model
    return extera


favorite_car = buy(manifacture='BMW', model="Z4", production_year=2022, color='Blue', price="I don't know")
print(favorite_car)


# ----------------------------------------------------------------------------------------
print("self study and search about *argv and k")


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
