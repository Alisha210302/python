# Prompt the user to enter their age
age = int(input("Enter the age: "))
if age>=1 and age<=110:
    if age<=5:
        print("Ticket is free")
    elif age>5 and age<=12:
        print("Ticket price is Rs.5")
    elif age>13 and age<=60:
        print("Ticket price is Rs.10")
    elif age>60:
        print("Ticket price is Rs.7")
    else:
        pass
else:
    print("Invalid age")