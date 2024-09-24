class Book:
    available = 1
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def display_details(self):
        print(f"title:{self.title} , author = {self.author} , year = {self.year}")
    def borrow_book(self):
        available = 0
        print(f"The book {self.title} has been borrowed")
    def return_book(self):
        available = 1
        print(f"The book {self.title} is now available")

b1 = Book("Pride and Prejudice","Jane Austen",1813)
b1.display_details()
b2 = Book("Dollar Bahu","Sudha Murthy",2001)
b2.display_details()
b2.borrow_book()
b2.return_book()


