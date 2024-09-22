def mysum(*args):
    positive_args = [num for num in args if num >= 0]
    return sum(positive_args)

print(mysum(3,4,-4))