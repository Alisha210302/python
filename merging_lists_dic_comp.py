keys = ['name','age','city']
values = ['Alice',25,'New York']
dic = {}
for i in range(len(keys)):
    dic[keys[i]] = values[i]
print(dic)

# using dictionary comprehension
dic1 = {keys[i]:values[i] for i in range(len(keys))}
print(dic1)