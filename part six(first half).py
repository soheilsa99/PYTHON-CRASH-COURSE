alien_0 = {"color": "green", "point": 5}
print(alien_0['color'])
print(alien_0['point'])
# single value
alien_0 = {"color": "green"}
print(alien_0['color'])
# -------------------------------------------------------------------------------------
alien_0 = {"color": "green", "point": 5}
new_points = alien_0["point"]
print(f"You just earned {new_points} points")
# Adding new Key_Value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
in dictionary we don't have sorted such as a list ans we can call the value with its key
"""
print("-----------------------------------------------------------------------------------")
# Starting with an Empty Dictionary (for example we have dynamic website)
alien_0 = {}
alien_0["color"] = "green"
alien_0["point"] = 5
print(alien_0)
print("-----------------------------------------------------------------------------------")
alien_0 = {"color" : "green"}
print(f"The alien is {alien_0['color']}.")
# we can change the value
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")
print("-----------------------------------------------------------------------------------")
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'slow'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
# Use del dictionary[key] to delete a key-value pair in a dictionary
alien_0 = {"color": "green", "point": 5}
print(alien_0)
del alien_0['point']
print(alien_0)
print("good example for store the information")
# store on kind of information about many object
f_language = {
    'sarah' : 'python',
    'edward': 'c++',
    'jen' : 'c#',
}
print(f_language)
language = f_language['sarah'].title()
print(f"sara favorite language is : {language}")
"""
when we don't know one key is consist in dictionary
we can use .get('value') 
"""
print(f_language.get('jen' , 'No such user'))
print(f_language.get('jenny' , 'No such user'))
print("-----------------------------------------------------------------------------------")
print("practice one : Person ")
new = {}
new['lovely friend'] = 'Hosein'
new['family name'] = 'Khatib'
new['girl friend'] = 'Fatemeh'
new['age'] = 34
new['city'] = 'New York'
print(new)
print(new['lovely friend'])
print(new['family name'])
print(new['girl friend'])
print(new['age'])
print(new['city'])
print("-----------------------------------------------------------------------------------")
print("practice two : Favorite Numbers ")
f_n = {"Ali" : 34, "Saman" : 18, "Homayon": 85, "Sadegh" : 8, "Sara" : 72}
print(f_n["Ali"])
print(f_n["Saman"])
print(f_n["Homayon"])
print(f_n["Sadegh"])
print(f_n["Sara"])
print("-----------------------------------------------------------------------------------")
print("practice three : Glossary ")
glossary = {
    "string" : "character variable",
    "integer" : "numerical variable",
    "list" : "ordered sequence of element",
    "dictionary" : "collection of key_value",
    "tuple" : "constant list"
}
print(f"string: {glossary['string']}.\n")
print(f"Integer: {glossary['integer']}.\n")
print(f"List: {glossary['list']}.\n")
print(f"Dictionary: {glossary['dictionary']}.\n")
print(f"Tuple: {glossary['tuple']}.\n")
print("-----------------------------------------------------------------------------------")
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value :{value}")
# we van also use shorter word
for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value :{v}")

print("-----------------------------------------------------------------------------------")
# if we need to print all value and key with sort an additional details we use 2 variable
favorite_language = {
    "jen" : "c++" ,
    "sarah" : "c" ,
    "edward" : "c#" ,
    "daniel" : "python",
    "samuel" : "Python",
}
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
friends = ["edward",'samuel']
for name in favorite_language.keys():
    print(f"Hi{name.title()}")
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you live {language}")
for name in sorted(favorite_language.keys()):
    print(f"{name.title()},thank you for taking the poll.")
print('The following language have been mentioned:')
for language in favorite_language.values():
    print(language)
for language in set(favorite_language.values()):
    print(language.title())