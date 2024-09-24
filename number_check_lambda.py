lst = [10,-1,34,6,0,-4,23]

num = map(lambda x:'positive' if x>0 else 'negative' if x<0 else 'zero' ,lst)
print(list(num))
