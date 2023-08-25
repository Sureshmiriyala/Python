#sum of integers
str = input("enter input:")
sum = 0 
for i in str:
    if i.isdigit():
        sum += int(i)
        print(sum)
        

