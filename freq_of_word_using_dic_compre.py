lst = ['apple','banana','apple','orange','banana','apple']
dict = {}
for i in lst:
    n = lst.count(i)
    dict[i] = n
print(dict)

# using the dictionary comprehension
dic1 = {i:lst.count(i) for i in lst}
print(dic1)