class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: Rs.{self.salary}")

# Example usage
p1 = Person("John", 30, 50000)
p2 = Person("Jane", 28, 55000)
p1.display()
p2.display()
