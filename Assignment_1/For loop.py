#example 1: Series of numbers

n = 9
for i in range(1,n+1):
    print(i)

for i in range(1,n+1):
    print(i,end="")

# example 2: creating Table by using for loop
num = int(input("enter input:"))
counter = 1
for i in range(1,11):
    print(num,"x",counter,"=",num*counter)
    counter = counter + 1