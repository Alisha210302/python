dic = {}
text = "Hello I am Alisha".split(' ')
# for i in text:
#     dic[i] = len(i)
# print(dic)
dic1 = {i:len(i) for i in text}
print(dic1)