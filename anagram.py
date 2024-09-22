s1 = input("Enter string1: ").lower()
s2 = input("Enter string2: ").lower()

if sorted(s1) == sorted(s2):
    print("They are anagrams")
else:
    print("They are not anagrams")



