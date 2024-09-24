text = input("Enter the text: ").split(' ')
# dict = {}
# for i in text:
#     dict[i] = len(i)
# print(dict)

# using dictionary comprehension
dic1 = {i:len(i) for i in text}
print(dic1)