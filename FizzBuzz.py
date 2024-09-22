lst = []
for i in range(1,21):
    lst.append(i)

# Fizz 3
# Buzz 5
# both FizzBuzz
# check the code
for i in range(len(lst)):
    if lst[i]%3 == 0 and lst[i]%5 == 0:
        lst[i] = 'FizzBuzz'
    elif i%5 == 0:
        lst[i] = 'Buzz'
    elif i%3 == 0 :
        lst[i] = 'Fizz'
print(lst)

# by using list comprehensions

l1 = ['FizzBuzz' if i%3 == 0 and i%5==0 else 'Buzz' if i%5==0 else 'Fizz'if i%3==0 else i for i in range(1,21) ]
print(l1)