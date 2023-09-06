# Write a Python script to add a key to a dictionary
d = {0:10, 1:20}
d[2] = 30   # adding one more key & value pair to dict
print(d)
# both ways , we can add the pair 
d.update({2:30})
print(d)

# Write a Python script to check whether a given key already exists in a dictionary
dic = {'a':10,'b':20,'c':30}

print(dic.get('b'))
 # method-2:
def check_key(dic,key):
    if key in dic.keys():
        print("Present, ",end="")
        print("value =",dic[key])
    else:
        print("Not Present")
key = 'd'
check_key(dic,key)

# Write a Python program to iterate over dictionaries using for loops
dic3 = {'a':101,'b':102,'c':103}
for key,value in dic3.items():
    print(key,value)

#method-2:
for key in dic3:
    print(key,dic3[key])

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
d=dict()
for x in range(1,16):
    d[x]=x*x
print(d)

# Write a Python program to create a dictionary from a string & count of the characters present in the string
str = input("enter a str:")
dic = {}
for char in str:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1 
print(dic)

# Write a Python program to sum all the items in a dictionary
# using values fun()
dict = {'a': 10, 'b': 20, 'c': 30}
def sum(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum
print("Sum :", sum(dict))

# using iteration of each value
def sum(dict):
 
    sum = 0
    for i in dict:
        sum = sum + dict[i]
 
    return sum
print("Sum :", sum(dict))

# Write a Python program to combine two dictionary by adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200, 'd':400}  
d3 = d2  
for i, j in d1.items():  
    if i in d2:  
        d3[i] = j + d2[i]  
    else:   
        d3[i] = j  
print(d3)  

# Write a Python program to access dictionary key's element by index
sub_score = {'physics': 75, 'math': 82, 'chemistry': 78}
print(list(sub_score)[0])
print(list(sub_score)[1])
print(list(sub_score)[2])

# Write a Python script to merge two Python dictionaries.d
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)