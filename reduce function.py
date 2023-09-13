# getting addition of numbers using map() function:
from functools import reduce 

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans)

# getting product of numbers using map() function:
def product(x,y):
    return x*y

ans = reduce(product, [2, 5, 3, 7])
print(ans)

# simple addition using map()
l = [1, 3, 5, 6, 2]
print(reduce(lambda a, b: a+b, l))

# to get the maximum number from the list
l = [1, 3, 5, 6, 2]
print(reduce(lambda a, b: a if a > b else b, l))