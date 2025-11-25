# class Employee:
#     # initialize name
#     def __init__(self,name):
#         self.name=name

#     #functions
#     def greet(self,name):
#         print(f"Good Morning {name} ")

# Abhi=Employee("Abhi")
# Abhi.greet()
# # Abhi.greet("Abhi")


##____________________________________________________________________________
#example 2

# class Book:
#     def __init__(self,title,author,isbn,price,qty):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.price=price
#         self.qty=qty

#     def displayBook(self):
#         print(f"{self.title} - {self.author} - {self.isbn}")

#     def calculateprice(self):
#         return self.price*self.qty
    
# book1=Book("who will cry when you die","Robin Sharma",265686,255,36)
# book2=Book("focus","stephn",2523232,66,24)

# book1.displayBook()
# book2.displayBook()
# print(f"{book1.title} total_price is {book1.calculateprice()}")


##____________________________________________________________________________
#example 3

class person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"{self.name}  - {self.c_no}")
class Employee(person):
    def __init__(self, name, c_no,salary):
        super().__init__(name, c_no)
        self.salary=salary
    def displayEmp(self):
        print(f"{self.name} - {self.c_no} - {self.salary}")

p1=person("abhi",252)
p1.display()
emp1=Employee("Abhijit",12556,669633)
emp1.display()
emp1.displayEmp()
# emp1.displayEmp(234)
