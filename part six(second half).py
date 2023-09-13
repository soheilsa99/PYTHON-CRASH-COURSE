# print("practice four Glossary 2")
# glossary = {
#     "string" : "character variable",
#     "integer" : "numerical variable",
#     "list" : "ordered sequence of element",
#     "dictionary" : "collection of key_value",
#     "tuple" : "constant list"
# }
# # print(f"string: {glossary['string']}.\n")
# # print(f"Integer: {glossary['integer']}.\n")
# # print(f"List: {glossary['list']}.\n")
# # print(f"Dictionary: {glossary['dictionary']}.\n")
# # print(f"Tuple: {glossary['tuple']}.\n")
# """
# in this practice we use a for loop to use a less print order
# """
# for key, value in glossary.items():
#     print(f"{key.title()}: {value}")
# print("-----------------------------------------------------------------------------------")
# print("practice five Rivers")
# rivers = {"Nile" : "Egypt" , "Amazon" : "Brazil" , "Mississippi" : "Usa"}
# for river, country in rivers.items():
#     print(f"The {river.title()} run through {country}")
# print("\n")
# for river in rivers.keys():
#     print(river.title())
# print("\n")
# for country in rivers.values():
#     print(country.title())
# print("-----------------------------------------------------------------------------------")
# print("practice six Polling")
# favorite_language = {
#     "jen" : "c++" ,
#     "sarah" : "c" ,
#     "edward" : "c#" ,
#     "daniel" : "python",
#     "samuel" : "Python",
# }
# people = ['jen' , 'sarah' , 'daniel' , 'soheil' , 'kity']
# for person in people:
#     if person in favorite_language.keys():
#         print(f"Hey, {person.title()}, thank you for taking the poll.")
#     else:
#         print(f"Hey, {person.title()}, please take the poll.")
# print("-----------------------------------------------------------------------------------")
# # my self practice
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color' : 'green' , 'point' : 5 , 'speed' : 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['point'] = 10
# for alien in aliens[:5]:
#     print(alien)
# print("-----------------------------------------------------------------------------------")
# # continue the book
# """
# Nesting : we can print many dictionary with use
# a name of dictionary as element of one list
# """
#
# alien_0 = {"color" : "green" , "point" : 5}
# alien_1 = {"color" : "gray" , "point" : 55}
# alien_2 = {"color" : "pink" , "point" : 875}
# aliens = [alien_0 , alien_1 , alien_2]
# for alien in aliens :
#     print(alien)
# print("-----------------------------------------------------------------------------------")
# aliens = []
# for alien_number in range(30):
#     new_alien = {"color" : "green" , "points" : 5 , "speed" : "slow"}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
#
#
# for alien in aliens[:5]:
#     print(alien)
#
# print(f"Total number of aliens : {len(aliens)}")
# print("-----------------------------------------------------------------------------------")
# """
# we can use a list as value in dictionary
# """
# pizza = {
#     'crust' : 'thick',
#     'toppings' : ["mushrooms", "extra cheese"]
# }
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")
#
# print("-----------------------------------------------------------------------------------")
# """
# we can use a dictionary as value in dictionary
# """
# user = {
#     "aeinstein" :
#     {
#        "first" : "Albert" ,
#         "last" : "aeinstein",
#         "location" : "princton"
#     },
#     'curie' : {
#         'first' : 'marie',
#         "last" : 'curie',
#         'location' : 'paris'
#     }
# }
# for username, user_info in user.items():
#     print(f"\n Username : {username}")
#     f_name = f"{user_info['first']}{user_info['last']}"
#     location = user_info['location']
#     print(f"\n Username: {f_name.title()}")
#     print(f"\n location: {location.title()}")
# print("-----------------------------------------------------------------------------------")
# print("practice seven People")
# information1 = {
#                 "first name" : "Ahmadreza" ,
#                 "last name" : "Andalib" ,
#                 "city" : "Esfahan" ,
#                 "nick name" : "bolbol" ,
#                 "job" : "math teacher"
#                 }
# print(information1)
# print(information1.keys())
# print(information1.values())
# information2 = {"first name" : "homayon" ,
#                 "last name" : "azizi" ,
#                 "city" : "esfahan" ,
#                 "nick name" : "joe" ,
#                 "job" : "chimistery teacher"}
# information3 = {"first name" : "Ahmad" ,
#                 "last name" : "Mirlohi" ,
#                 "city" : "esfahan" ,
#                 "nick name" : "haji" ,
#                 "job" : "Dentist"}
# print(information2)
# print(information3)
# b = []
# b.append(information1)
# b.append(information2)
# b.append(information3)
# print(b)
# person = [information2, information1, information3]
# print("\n person")
# for i in person :
#     print("-------------------------------------------------------------------------")
#     print('first name :', i['first name'])
#     print('last name :' , i['last name'])
#     print('city :', i['city'])
#     print('nick name :', i['nick name'])
#     print('job :', i['job'])
# print("-------------------------------------------------------------------------")
# print("practice eight Pets")
#
# pet0 = {"owner" : "sam", "animal" : "cat"}
# pet1 = {"owner" : "hesam", "animal" : "hamster"}
# pet2 = {"owner" : "gabriel", "animal" : "dog"}
# pet3 = {"owner" : "david", "animal" : "rabbit"}
# pet4 = {"owner" : "sara", "animal" : "fish"}
# pet5 = {"owner" : "soheil", "animal" : "parrot"}
#
# pets = [pet0, pet1, pet2, pet3, pet4, pet5]
# for pet in pets:
#     print(f"The pet is a {pet['animal']}.The owner is : {pet['owner']}")
# print("-------------------------------------------------------------------------")
# print("practice nine Favorite Place")
# favorite_place = {"Amir" : ["Taj mahal", "Azady square", "cofe denje"],
#                     "Samuel" : ["honar park", "coffe denje", "art museum"],
#                     "Soheil" : ["art university", "cofe denje", "Azady square"]
#                   }
# for name, places in favorite_place.items():
#     print(f"{name.title()}'s favorite place are :")
#     for place in places:
#         print(f"\t{place.title()}")
#     print("\n")
#
#
# print("-------------------------------------------------------------------------")
# print("practice ten Favorite Numbers")
# """
# we  use the practice two "Favorite Numbers" , update  people can have many favorite number
# """
# f_n = {"Ali" : 34, "Saman" : [18, 23, 45] , "Homayon": [85, 23] , "Sadegh" : 8, "Sara" : 72}
# for name, numbers in f_n.items():
#     print(f"{name.title()}'s favorite numbers are: ")
#     for number in numbers:
#         print(f"\t{number}")
#     print("\n")
print("-------------------------------------------------------------------------")
print("practice eleven : Cities\n")
cities = {
    "Esfahan" : {'country' : 'Iran', 'population': 'two million', 'fact' : 'one of the must beautiful city each person should see '},
    "Tehran" : {'country' : 'Iran', 'population': 'nine million', 'fact' : 'The capital city of Iran '},
    "New York" : {'country' : 'US', 'population': 'eight million and five hundred thousand', 'fact' : 'One of the must important city in US '}
}
for city, details in cities.items():
    print(f"{city.title()} is located in {details['country']}")
    print(f"has a population of {details['population']}")
    print(f"Fact about {city.title()}: {details['fact']}\n")
print("-------------------------------------------------------------------------")
print("practice twelve : Extension \n")
glossary = {
    "string" : "character variable",
    "integer" : "numerical variable",
    "list" : "ordered sequence of element",
    "dictionary" : "collection of key_value",
    "tuple" : "constant list",
    "set" : "collection of member that out of sorts",
    "function " : "block of code that performs a specific task"
}

for k , v in glossary.items():
    print(f"{k.title()} :")
    print(f"{v}\n")