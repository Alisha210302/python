# Split the text into a list (note that splitting by ',' won't work here; we'll split by spaces)
text = 'hello world hello world'.split(' ')
lst = text.copy()  # Make a copy if you want to keep the original

# Replace elements at even indices
for i in range(len(lst)):
    if i % 2 == 0:
        lst[i] = 'replaced'  # Replace the element at the even index

print(lst)
