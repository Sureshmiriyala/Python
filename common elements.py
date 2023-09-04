list_1 = list(eval(input('enter input:')))
list_2 = list(eval(input('enter input:')))

intersect = set(list_1) & set(list_2)
if intersect:
    print("True")
else:
    print("False")

