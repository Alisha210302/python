num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
choice = int(input("Enter the operation you want to preform: \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n"))

if choice==1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice==2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice==3:
    print(f"{num1} * {num2} = {num1*num2}")
elif choice==4:
    print(f"{num1}/{num2} = {num1/num2}")
else:
    print("Invalid choice")