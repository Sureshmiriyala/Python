# # To print Unique characters from a string:
# string = input("enetr string:")
# unique_chars = set()

# for char in string:
#     if char not in unique_chars:
#         unique_chars.add(char)
# print(unique_chars)

# # to print Non-repeated characters in a string:
# string = input("enter a string:")
# unique_chars = []

# for char in string:
#     if char not in unique_chars:
#         unique_chars.append(char)

# result = ''.join(unique_chars)
# print(result)

# # Creating a copy of string into another string:
# string = input("enter a string:")
# new_string = string[:]
# # print(new_string)

# string = input("enter a string:")
# string2 = ""
# for char in string:
#     string2 = string2 + char
# print(string2)

# # To print the string character in ascending order:
# string = input("enter a string:")
# sort_string = sorted(string)

# for char in sort_string:
#     print(char,end="")

# # using Recursion to get fibonacci series sum upto Nth term:
# def fib(i):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return fib(i-2) + fib(i-1)
# i = int(input("enter the fibonacci number:"))
# print(fib(i))

# # Add a key to a dictionary:
# d = {'a':10,'b':20}
# d['c']=30
# print(d)

# d1 = {1:100,2:200,3:300}
# d1.update({4:400})
# print(d1)
 
# # To check the given key is present in a dictionary or not:
# d2 = {'a': 10,'b': 20,'c': 30}
# print(d2.get('d'))

# d2 = {'a': 10,'b': 20,'c': 30}
# def check_key(d2,key):
#     if key in d2.keys():
#         print("Present")
#     else:
#         print("Not Present")
# key = 'd'
# check_key(d2,key)

# #print a dictionary where the keys are numbers between 1 to 15 and the values are the square of the keys
# dic = dict()
# for x in range(1,16):
#     dic[x]=x*x
# print(dic)

# # To sum all the items in a dictionary:
# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# def sum(dic):
#     sum = 0
#     for i in dic.values():
#         sum = sum + i
#     return sum

# print(sum(dic))

# #To combine two dictionaries by adding values for common keys:
# d1 = {'a': 100, 'b': 200, 'c':300}  
# d2 = {'a': 300, 'b': 200, 'd':400} 
# d = d2

# for key,value in d1.items():
#      if key in d2:
#          d[key]=value+d2[key]
#      else:
#          d[key] = value
# print(d)
    
# merge of two Python dictionaries:
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'x': 600, 'y': 700, 'z':800} 

d1.update(d2)
print(d1)


         

