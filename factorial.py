n = int(input("Enter the number you want to find the factorial of: "))
result = 1
for i in range(1,n+1):
    result *=i

print(result)