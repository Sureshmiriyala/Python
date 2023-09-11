# print the given numbers is multiple of 5
numbers = eval(input('enter numbers:'))
result = list(filter(lambda x: x % 5 == 0, numbers))
print(result)

# check the given numbers is multiple of 3 and is multiple of 5 
num = eval(input('enter numbers:'))
result = filter(lambda x : True if x%3==0 and x%5==0 else False,num)
print(list(result))

# print the numbers, which are greater than 10
lst = eval(input('enter numbers:'))
lst2 = list(filter(lambda x:(x>10),lst))
print(lst2)