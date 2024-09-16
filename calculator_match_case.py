n = 1
while n:
    num1 = float(input("Enter the num1: "))
    num2 = float(input("Enter the num2: "))
    choice = int(input("Enter the operation you want to perform:\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n"))

    match choice:
        case 1:
            print(f"Addition of {num1} and {num2} is {num1+num2}")
        case 2:
            print(f"Subtraction of {num1} and {num2} is {num1-num2}")
        case 3:
            print(f"multiplication of {num1} and {num2} is {num1*num2}")
        case 4:
            print(f"Division of {num1} and {num2} is {num1/num2}")
        case _ :
            print("Enter valid operation")

    n = int(input("Press 1 to continue and 0 to exit"))