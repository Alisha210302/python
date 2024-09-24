lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = []
for i in lst:
    if i%2 == 0:
        square = i**2
        lst1.append(square)
    else:
        cube = i**3
        lst1.append(cube)
print(lst1)

# using list comprehension
l = [i**2 if i%2==0 else i**3 for i in lst ]
print(l)