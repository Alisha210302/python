l1 = [
    [1, 2, 3],
    [4, 5, 6]
]

l2 = [
    [7, 8, 9],
    [10, 11, 12]
]

# Initialize the result matrix with zeros
l3 = [[0 for _ in range(len(l1[0]))] for _ in range(len(l1))]

# Perform matrix addition
for i in range(len(l1)):
    for j in range(len(l1[0])):
        l3[i][j] = l1[i][j] + l2[i][j]

# Print the result
print(l3)
