class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: Rs.{self.cost}")

# Example usage
b = Book()
b.get_details("Python Basics", "Guido van Rossum", 350)
b.print_details()
