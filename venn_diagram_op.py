fruits = {'apple','banana','tomato','watermelon'}
vegetables = {'tomato','potato','spinach','drumstick'}
grains = {'jowar','bajra','tomato','raggi'}

# common to all (intersection)
common = grains.intersection(fruits.intersection(vegetables))
print(f"Common among all is {common}")

# not common to any (symmetric difference)
not_common = grains.symmetric_difference(fruits.symmetric_difference(vegetables))
print(f"The not common things are {not_common}")

# unique items (difference)
uniq = grains.difference(fruits.difference(vegetables))
print(f"The unique elements are {uniq}")