tup = input("Enter the elements comma seperated: ").split(',')
tup1 = tuple(tup)
print(tup1)
num = input("Enter the element to repeat: ")
repeat = []
for i in tup:
    repeat.append(i)
    if i == num:
        repeat.append(i)
repeated_tuple = list(repeat)
print(repeated_tuple)