class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"{self.model} ({self.year}) costs Rs.{self.price}")

# Example usage
car1 = Car("Toyota", 2020, 800000)
car2 = Car("Hyundai", 2022, 900000)
car1.cost()
car2.cost()
