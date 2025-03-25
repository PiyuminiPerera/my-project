from car import Car

car1 = Car('Toyota','Corolla',2022)
car2 = Car('Honda','Civic',2021)
print('Hello,Here are car details:')
print(car1.display_info())
print(car2.display_info())

print(compare_cars(car1, car2))
