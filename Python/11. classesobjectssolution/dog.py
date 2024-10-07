class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} is rolling over')

my_dog = Dog('Jackie', 12)
print(f"My dog's name is '{my_dog.name}' and he is '{my_dog.age}'")
my_dog.sit()
my_dog.roll_over()