class User:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(f'{full_name} is logged in successfully')
        print(f"{full_name}'s password is {self.password}")

    def greet_user(self):
        print(f'Welcome back {self.first_name + ' ' + self.last_name}') 

user = User('Anoop', 'George', '1234')
print(f'{user.first_name + ' ' + user.last_name} signed in with password {user.password}')
user.describe_user()
user.greet_user()
