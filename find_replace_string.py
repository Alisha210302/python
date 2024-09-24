# Sample text
text = "Hello world! Welcome to the world of programming. The world is vast."

# Substring to find and replace
substring = "world"
replacement = "universe"

# 1. Find the First Occurrence of a Substring
first_index = text.find(substring)
print(f"First occurrence of '{substring}': Index {first_index}")

# 2. Find All Occurrences of a Substring
# Using a loop to find all occurrences
all_indices = []
start = 0
while True:
    start = text.find(substring, start)
    if start == -1:
        break
    all_indices.append(start)
    start += 1  # Move past the last found index

print(f"All occurrences of '{substring}': Indices {all_indices}")

# 3. Replace First Occurrence of a Substring
text_first_replaced = text.replace(substring, replacement, 1)
print("After replacing the first occurrence:", text_first_replaced)

# 4. Replace All Occurrences of a Substring
text_all_replaced = text.replace(substring, replacement)
print("After replacing all occurrences:", text_all_replaced)
