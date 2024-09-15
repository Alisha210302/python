# Factorial of a number: using for loop, while loop
num = int(input("Enter the number to find the factorial: "))
fact = 1
# using for loop
for i in range(1,num+1):
    fact = fact*i
print(fact)

# using while loop

while num<=1:
    fact = 1
    fact = fact*num
    num-=1
print(fact)