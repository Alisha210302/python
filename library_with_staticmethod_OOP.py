class Book:
    available = 1
    @classmethod
    def num_of_copies_available(cls):
        return cls.available
    @staticmethod
    def Best():
        print("books are man's best friend")


    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def display_details(self):
        print(f"title:{self.title} , author = {self.author} , year = {self.year}")
    def borrow_book(self):
        if Book.available >0:
            print(f"The book {self.title} has been borrowed")
        else:
            print("The book is not available for borrowing")
    def return_book(self):
        Book.available +=1
        print(f"The book {self.title} is now available")

b1 = Book("Pride and Prejudice","Jane Austen",1813)
b1.display_details()
b2 = Book("Dollar Bahu","Sudha Murthy",2001)
b2.display_details()
b2.borrow_book()
b2.return_book()
b2.num_of_copies_available()
print(f"Copies available:{Book.num_of_copies_available()}")
b2.Best()


