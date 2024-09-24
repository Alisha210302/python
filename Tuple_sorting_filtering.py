num = input("Enter the list of numbers: ").split(',')
print(num)
lst = [int(x) for x in num]
print(lst)
tup = tuple(lst)
print(tup)
tup1 = sorted(tup)
print(tup1)
l1 = list(tup1)
l2 = []
for i in l1:
    if i<7:
      l2.append(i)
      print(f"l2 is modified {l2}")
    else:
        print(tuple(l1))