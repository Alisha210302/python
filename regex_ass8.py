import re
expression = r'\b^[aeiouAEIOU]\w*[bcdefghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b'

with open('regex.txt','r') as file:
    content = file.read()
print(content)
content1 = re.findall(expression,content,re.MULTILINE)
print(content1)

ex = r'[\d]+[\D]'
content2 = re.findall(ex,content,re.MULTILINE)
print(content2)

ex1 = r'^Note.*!$'
content3 = re.findall(ex1,content,re.MULTILINE)
print(content3)