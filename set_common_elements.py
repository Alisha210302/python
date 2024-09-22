tup1 = (1,2,3,4,5,6)
tup2 = (1,2,3,7,8,9)

s1 = set(tup1)
s2 = set(tup2)

inter = s1.intersection(s2)
print(f"Common elements in tuple are {inter}")