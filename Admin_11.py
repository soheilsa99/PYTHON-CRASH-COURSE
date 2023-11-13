
"""I use the code of exercise seven as base
 and customize it for this practice"""


class User:
    def __init__(self, age, id, name, family):
        """Initialize user class with much information attributes. """
        self.age = age
        self.id = id
        self.name = name
        self.family = family

    def describe_user(self):
        """Describe a user"""
        print(f"The user name is {self.name} {self.family}")
        print(f"The user is {self.age} years old")

    def greet_user(self):
        """Greeting to user"""
        print(f"Hi {self.name.title()} {self.family}")


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges"""
        print("privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, age, id, name, family, privileges):
        super().__init__(age, id, name, family)
        self.privileges = Privileges(privileges)


admin = Admin('Soheil', 'Admin', 'nbc', 21, ['can add post', 'can delete post', 'can be user'])
admin.privileges.show_privileges()