class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges"""
        print("privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

