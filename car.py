class Car:
    
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

   def display_info(self):
       return f"{self.year} {self.brand} {self.model} - ${self.price}"

   
