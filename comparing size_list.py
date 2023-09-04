list1 = list(eval(input('enter input:')))
list2 = list(eval(input('enter input:')))

list1.sort()
list2.sort()
 
if list1 == list2:
    print("The lists are same")
else:
    print("The lists are not same")