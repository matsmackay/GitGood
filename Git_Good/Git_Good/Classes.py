#Classes file

class User:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.fullname = self.surname + " " + self.name

    def return_full_name(self):
        print("Your username is {}.".format(self.fullname))

# Commented out for later use
# surname = input('What is your surname?: ').upper()
# name = input('What is your last name?: ').upper()
# user = User(surname, name)

user = User('PIET','HEIN')
user.return_full_name()
