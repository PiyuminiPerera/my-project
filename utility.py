def compare_years(car1, car2):
    if car1.year > car2.year:
        return f"{car1.brand} {car1.model} is newer."
    elif car1.year < car2.year:
        return f"{car2.brand} {car2.model} is newer."
    else:
        return "Both cars are from the same year."

def compare_prices(car1, car2):
    if car1.price > car2.price:
        return f"{car1.brand} {car1.model} is more expensive."
    elif car1.price < car2.price:
        return f"{car2.brand} {car2.model} is more expensive."
    else:
        return "Both cars cost the same."
