collection = {}

def add():
    values = {}
    title,author,genre,year = input("Enter the title,author,genre,year comma separated: ").split(',')
    values['author'] = author
    values['genre'] = genre
    values['year'] = year
    collection[title] = values

def remove():
    to_remove = input("Enter the book name you want to remove: ")
    if to_remove in collection:
        del collection[to_remove]


def search():
    to_search = input("enter by what you wish to search to by genre or author: ")
    value = input("Enter the value of it: ")

    found_book = []
    if to_search == "genre":
        for title,info in collection.items():
            if info['genre'] == value:
                found_book.append(title)
    elif to_search == "author":
        for title,info in collection.items():
            if info['author'] == value:
                found_book.append(title)
    else:
        print("Invalid search")
    if found_book:
        for b in found_book:
            print(f"Books found are {b}")
    else:
        print("No books found!")


add()
add()
remove()
search()