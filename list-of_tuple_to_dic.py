lst = []
dic = {}
while True:
    wish = input("Do you want to exit press 0 ")
    if wish == '0':
        break
    k = input("Enter the key: ")
    v = input("Enter the value: ")
    tup = (k,v)
    lst.append(tup)
    print(lst)

    for i in lst:
        k,v = i
        dic[k] = v
        print(dic)
