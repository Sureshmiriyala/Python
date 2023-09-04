# write a python program to delete given elemet from the list 
list = list(eval(input('enter input:')))
list.remove(3)
print(list)

# using list comprehension:
new_list = [i for i in list if i !=3]
print(new_list)