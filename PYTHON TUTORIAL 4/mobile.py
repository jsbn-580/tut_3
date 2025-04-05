class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: Rs.{self.price}")

# Example usage
m = Mobile()
m.set_details("Samsung", "Galaxy A14", 15000)
m.display_details()
