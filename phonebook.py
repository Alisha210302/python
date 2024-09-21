phone_book = {}

def add_info():
    name, phone, email = input("Enter the name,phone number and email seperated by commas: ").split(',')
    info = {}
    info['phone'] = phone
    info['email'] = email
    phone_book[name] = info

def search_info():
    s_name = input("Enter the name of person you want to search: ")
    if s_name in phone_book:
        info = phone_book[s_name]
        print(f"Name: {s_name}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        print("Contact not found.")

def update_info():
    s_name = input("Enter the name of the person you want to update: ")
    if s_name in phone_book:
        field = input("Enter what do you want to update: name, phone, or email: ")
        if field == "name":
            new_name = input("Enter the new name: ")
            phone_book[new_name] = phone_book.pop(s_name)  # Update the key
            print(f"Updated name from {s_name} to {new_name}.")
        elif field == "phone":
            new_phone = input("Enter the new phone number: ")
            phone_book[s_name]['phone'] = new_phone
            print(f"Updated phone number for {s_name}.")
        elif field == "email":
            new_email = input("Enter the new email: ")
            phone_book[s_name]['email'] = new_email
            print(f"Updated email for {s_name}.")
        else:
            print("Invalid field. Please enter 'name', 'phone', or 'email'.")
    else:
        print("Contact not found.")

def delete_info():
    d_name = input("Enter the name of the person you want to delete: ")
    if d_name in phone_book:
        del phone_book[d_name]
    print(phone_book)

add_info()
add_info()
update_info()
search_info()
delete_info()


