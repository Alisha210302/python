lst = [1,2,3,1,1,1,2,2,5,6,7,5,6,8,9]
dic = {}
for i in lst:
    n = lst.count(i)
    dic[i] = n
print(dic)