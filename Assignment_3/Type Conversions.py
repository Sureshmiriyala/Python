# string to list conversion:
str = "Python has more features"
lst = list(str)
print(lst)

# Tuple to list:
tuple = (1,2,3,4,5,6)
my_list = list(tuple)
print(my_list)

tuple_1 =('c','c++','java','python')
my_list_1 =list(tuple_1)
print(my_list_1)

# converting range to list:
values = range(5,20)
list_range = list(values)
print(list_range)

values_2 = range(1,20,2)
list_range_2 = list(values_2)
print(list_range_2)

# converting dict to list:
dict = {1:'krishna',2:'rama',3:'visnu',4:'shiva'}
new_list = list(dict.items())           # using item() method
list_keys = list(dict.keys())           # using keys() method
list_values = list(dict.values())       # using values() method
list_cmprh = [i for i in dict.items()]  # using list comprehension method

new_lst = []
for i in dict.items():
    new_lst.append(i)
print(new_lst)
    
print(new_list)      
print(list_keys)     
print(list_values)  
print(list_cmprh) 




