class Car:
    
    def __init__(self, brand, model, year, price, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.speed = speed

    def display_info(self):
        return f"{self.year} {self.brand} {self.model} - ${self.price}, Top Speed:{self.speed} km/h"

   
