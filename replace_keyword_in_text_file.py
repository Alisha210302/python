with open('info.txt','r') as file:
    file_contents = file.read()


modified_contents = file_contents.replace('after','before')

with open('info.txt','w') as file:
    file.write(modified_contents)

