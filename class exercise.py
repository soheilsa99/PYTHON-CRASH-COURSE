print("-------------------------------------------------------------------------------")
print("Practice ten : Imported_restaurant")
from restaurant import Restaurant
restaurant1 = Restaurant('Sophia', 'French')
restaurant2 = Restaurant('Mia', 'Spain')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

print("-------------------------------------------------------------------------------")
print("Practice eleven : Imported_Admin")
from Admin_11 import Admin

admin = Admin('Soheil', 'Admin', 'nbc', 21, ['can add post', 'can delete post', 'can be user'])
admin.privileges.show_privileges()


print("-------------------------------------------------------------------------------")
print("Practice twelve : Multiple Modules")
from Admin_12 import Admin
from privileges_12 import Privileges

admin = Admin('Soheil', 'Admin', 'nbc', 21, ['can add post', 'can delete post', 'can be user'])
admin.privileges.show_privileges()