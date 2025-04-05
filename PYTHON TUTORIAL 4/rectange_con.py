class Arith:
    def read(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))

    def add(self):
        print("Sum:", self.a + self.b)

# Example usage
obj = Arith()
obj.read()
obj.add()
