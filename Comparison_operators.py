# ==, !=, >,<, >=, <=

a = int(input("Enter the num1: "))
b = int(input("Enter the num2: "))

if a==b:
    print("a and b are equal")
elif a!=b:
    print("a and b are not equal")
elif a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
elif a>=b:
    print("a is greater than or equal to b")
elif a<=b:
    print("a is less than or equal to b")
else:
    pass