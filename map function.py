 # returns the cubes of a number
num = [1, 2, 3, 4, 5]
def cubes(num):
  return num * num * num

cube_numbers = list(map(cubes,num))
print(cube_numbers)

# Passing Multiple Iterators to map() Using Lambda

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))