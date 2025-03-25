from car import Car

car1 = Car('Toyota','Corolla',2022,35000,220)
car2 = Car('Honda','Civic',2021,25000,200)
print('Hello,Here are car details:')
print(car1.display_info())
print(car2.display_info())

print(compare_prices(car1, car2))
print(compare_years(car1, car2))
print(compare_speed(car1, car2))
