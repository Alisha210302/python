scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 65}
dic = {}
for k,v in scores.items():
    if v>80:
        dic[k] = v+5
print(dic)

# using dictionary comprehension

dic1 = {k:v+5 for k,v in scores.items() if v>80}
print(dic1)
