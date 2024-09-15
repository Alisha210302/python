n = 1
while n:
    choice = int(input("Enter the choice for conversion:\n 1.Inches to feet\n 2.Inches to centimeters\n 3.Inches to meters\n"))
    if choice == 1:
        a = float(input("Enter the value in inches: "))
        feet = a*0.08333
        print(f"Conversion of {a}inches to {feet}feet")
    elif choice == 2:
        a = float(input("Enter the value in inches: "))
        centimeter = a * 2.54
        print(f"Conversion of {a}inches to {centimeter}cms")
    elif choice ==3:
        a = float(input("Enter the value in inches: "))
        meters = a * 0.0254
        print(f"Conversion of {a}inches to {meters}meters ")
    else:
        print("invalid choice")

    n = int(input("Do you wish to continue press 1 for continue and 0 for exit"))
