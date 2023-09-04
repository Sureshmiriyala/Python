lst_1 = [input('enter input:')]
lst_2 = [input('enter input:')]

for i in lst_2:
   lst_1.extend(lst_2)          # using extend method
print(lst_1)

for i in lst_2:
    lst_1.append(i)             # using append method
print(lst_1)

lst_3 = lst_1 + lst_2
print(lst_3)                    # using concatenation method

new_lst = [y for x in [lst_1,lst_2] for y in x]
print(new_lst)                  # using list comprehension method

