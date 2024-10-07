class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Name Of the Restaurant is {self.restaurant_name}')
        print(f'Cusine Types Available in this Restauant is {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is Open')

restaurant = Restaurant('Ocean Pearl', '[Nonv-veg, Veg, Chinese, Japanese]')
print(f'{restaurant.restaurant_name} is now open with cusines like {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('King Dine', ['Non Veg, European'])
print(f'{restaurant2.restaurant_name} is now open with cusines like {restaurant2.cuisine_type}')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Queens Dine', ['Non Veg, European'])
print(f'{restaurant3.restaurant_name} is now open with cusines like {restaurant3.cuisine_type}')
restaurant3.describe_restaurant()