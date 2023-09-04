lst = list(eval(input('enter input:')))
print(list(set(lst)))

# using list comprehension:
new_lst = [ lst[i] for i in range(len(lst)) if lst.index(lst[i]) == i]
print(new_lst)

