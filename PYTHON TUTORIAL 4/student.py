class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def dataprint(self):
        print(f"Name: {self.name}, Roll Number: {self.roll}")

# Example usage
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)
s1.dataprint()
s2.dataprint()
