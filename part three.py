food = ["ghorme sabzi","koko","kabab","gheime"]
print(food.sort())
print(food[0].title())
print(f"The first food that i was cook was {food[1].title()} It is vwery teisty")
# ------------------------------------------------------------------------------------
# all thing about count function
massage = "python popular programing language"
print(f'the number of p in that massage was : {massage.count("p")}')
# print(food.count()) , count function can't say a number of memeber of one list
# The target of cunt function is to count a specail alphabet in passage or how many same number use in one list
g = [11,22,31,312,11,11]
print(g.count(11))
# ------------------------------------------------------------------------------------
#practice 3_1
name = ["Saman","Javad","Amir","Ali"]
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
# ------------------------------------------------------------------------------------
#practice 3_2
name = ["Saman","Javad","Amir","Ali"]
print(f"Hi {name[-1]}, how are you")
print(f"Hi {name[-2]}, how are you")
print(f"Hi {name[-3]}, how are you")
print(f"Hi {name[-4]}, how are you")
# ------------------------------------------------------------------------------------
#practice 3_3
f_car = ["BMW","BENZ","TESLA"]
print(f'I would like to own a {f_car[2]}')
# ------------------------------------------------------------------------------------
#change element of list
print(f"The old name list was : {name}")
name[0] = "Mohamad"
print(f"The change list is : {name}")
#Add element
name.append("Sara")
print(name[-1])
#empty list
laptop_brand = []
laptop_brand.append("Acer")
laptop_brand.append("Asus")
laptop_brand.append("Apple")
laptop_brand.insert(2 ,'Lenovo')
print(laptop_brand)
#Delet element of list
del laptop_brand[0]
print(laptop_brand)
#if we use a pop method we delet a last element of list
print(f"The last compani in list is : {laptop_brand.pop()}")
#Use a remove method for delete a specific value from a list
print(f"i was deleet a Acer from brand list {laptop_brand}")
# ------------------------------------------------------------------------------------
# practice 3_4
invite = ["samuel","sara","jack","Arden","kit","azalea"]
print(f"Hi dear {invite[0]} ,You are invited for deinner")
print(f"Hi dear {invite[1]} ,You are invited for deinner")
print(f"Hi dear {invite[2]} ,You are invited for deinner")
print(f"Hi dear {invite[3]} ,You are invited for deinner")
print(f"Hi dear {invite[4]} ,You are invited for deinner")
print(f"Hi dear {invite[5]} ,You are invited for deinner")
# ------------------------------------------------------------------------------------
# practice 3_5
print(f' {invite[3]} can\'t com for dinner deinner')
invite.remove("Arden")
invite.append("Lili")
print(f"Hi dear {invite[0]} ,You are invited for deinner")
print(f"Hi dear {invite[1]} ,You are invited for deinner")
print(f"Hi dear {invite[2]} ,You are invited for deinner")
print(f"Hi dear {invite[3]} ,You are invited for deinner")
print(f"Hi dear {invite[4]} ,You are invited for deinner")
print(f"Hi dear {invite[5]} ,You are invited for deinner")
# ------------------------------------------------------------------------------------
# practice 3_6
print("We foun bigger table for dinner")
invite.insert(0 ,"Oliver")
invite.insert(4 ,"James")
invite.append("William")
print(f"Hi dear {invite[0]} ,You are invited for deinner")
print(f"Hi dear {invite[1]} ,You are invited for deinner")
print(f"Hi dear {invite[2]} ,You are invited for deinner")
print(f"Hi dear {invite[3]} ,You are invited for deinner")
print(f"Hi dear {invite[4]} ,You are invited for deinner")
print(f"Hi dear {invite[5]} ,You are invited for deinner")
print(f"Hi dear {invite[6]} ,You are invited for deinner")
print(f"Hi dear {invite[7]} ,You are invited for deinner")
print(f"Hi dear {invite[8]} ,You are invited for deinner")
# ------------------------------------------------------------------------------------
# practice 3_7
print("""
I can invite just two person for dinner:( 
Sorry ,my table will arrive late """
)
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
no = invite.pop()
print(f"Hi my dear frind {no} dinner is cancel")
print(f"Hi dear {invite[0]} ,You are still in invited list  for deinner")
print(f"Hi dear {invite[1]} ,You are still in invited list  for deinner")
del invite[0]
del invite[0]
print(f"The empty of inite list : {invite}")
# ------------------------------------------------------------------------------------
name = ["Saman","Javad","Amir","Ali"]
print(sorted(name))
name.sort()
print(name)
# name.sort(reverse=True) = name.reverse()
# number of item = len
print(len(name))
# ------------------------------------------------------------------------------------
# practice 3_8
place = ['Honolulu' ,'Golde_gate' ,'Clacier_National_Park'
         ,'Maui' ,'French_Quarter' ,'Niagara_Falls']
print(place)
b = sorted(place)
print(b)
# The orginal list don't have change
print(place)
place.reverse()
print(place)
# use 2 reverse change list to orginal list
place.reverse()
print(place)
# ------------------------------------------------------------------------------------
# practice 3_9
invite = ["Oliver","samuel","sara","jack","James","Arden","kit","azalea"]
print(f"There are {len(invite)} guest invited for dinner ")
# ------------------------------------------------------------------------------------
# practice 3_10
# we use invite list 3_9 for
invite.append("William")
invite.insert(-1 ,"Jimi")
del invite[-3]
invite.remove('samuel')
print(f" the number of guest is : {len(invite)}")
print(invite.sort())
# ------------------------------------------------------------------------------------
# practice 3_11
# index eror
city = ["Esfahan","Tehran","Yazd"]
print(city[5])