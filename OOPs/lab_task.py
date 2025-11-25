#1> Book add price, qty ,method calculatepricebook
# class Book:
#     # Constructor
#     def __init__(self, title, price, quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity

#     # Method to calculate total price
#     def calculate_total_price(self):
#         return self.price * self.quantity

#     # Method to display book details
#     def display(self):
#         print("\nBook Details")
#         print("------------")
#         print("Title:", self.title)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total Price:", self.calculate_total_price())

# # Main Program (Take input from user)
# title = input("Enter Book Title: ")
# price = float(input("Enter Book Price: "))
# quantity = int(input("Enter Quantity: "))

# # Create object of Book class
# b1 = Book(title, price, quantity)

# # Display result
# b1.display()

#_______________________________________
# class Book:
#     def __init__(self, price, qty):
#         self.price = price
#         self.qty = qty

#     def calculate(self):
#         return self.price * self.qty


# # Taking user input
# price = float(input("Enter price of book: "))
# qty = int(input("Enter quantity: "))

# # Create object
# b = Book(price, qty)

# # Print total price
# print("Total Price =", b.calculate())

##______________________________________________________________________________________
#2> create list of books
# class Book:
#     def __init__(self, title, author, price):    
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")
# # Create a list to store books
# books = []
# n = int(input("Enter number of books: "))
# for i in range(n):
#     title = input(f"Enter title of book {i+1}: ")
#     author = input(f"Enter author of book {i+1}: ")
#     price = float(input(f"Enter price of book {i+1}: "))
#     book = Book(title, author, price)
#     books.append(book)
# # Display all books
# print("\nBook List:")
# for book in books:
#     book.display()

##______________________________________________________________________________________
#3> create functions which accept authur and display those books
class Book:
    def __init__(self, title, author, price):    
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")
# Create a list to store books
books = []
n = int(input("Enter number of books: "))
for i in range(n):
    title = input(f"Enter title of book {i+1}: ")
    author = input(f"Enter author of book {i+1}: ")
    price = float(input(f"Enter price of book {i+1}: "))
    book = Book(title, author, price)
    books.append(book)
# Function to display books by a specific author
def display_books_by_author(author_name):
    print(f"\nBooks by {author_name}:")
    found = False
    for book in books:
        if book.author.lower() == author_name.lower():
            book.display()
            found = True
    if not found:
        print("No books found by this author.")
# Get author name from user and display books
author_name = input("Enter author name to search for books: ")
display_books_by_author(author_name)

##____________________________________________________________________________________________
#4> 
class distance:
    def __init__(self):
        pass
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch
    def __mul__(self,obj2):
        inch1=self.inch*obj2.inch
        feet1=self.feet*obj2.feet

        obj=distance(feet1,inch1)
        return obj
    def display(self):
        print(f"{self.feet} - {self.inch}")

d1=distance(5,5)
d2=distance(2,2)
d1.display()
d2.display()
d3=distance(0,0)
d3=d1*d2
d3.display()
    