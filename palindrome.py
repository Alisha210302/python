text = input("Enter any string: ").strip()
text_new = text.lower()
if text_new == text_new[::-1]:
    print("palindrome")
else:
    print("not palindrome")
