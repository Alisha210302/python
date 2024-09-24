import re
with open('read.txt','r') as file:
    info = file.read()
print(info)
expression = r'^Start.+End$'
match = re.findall(expression,info,re.MULTILINE)
print(match)