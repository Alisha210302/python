from numpy.ma.extras import average

num = input("Enter the list of numbers: ").split(',')
print(num)
lst = [int(a) for a in num]
print(lst)
tup = tuple(lst)
print(tup)

print("Sum of elements is: ",sum(tup))
print("Average of elements is: ",average(tup))
print("Max value in tuple is: ",max(tup))
print("Min value in tuple is: ",min(tup))
count = 0
for i in tup:
    count+=1
print(f"No of elements:{count}")