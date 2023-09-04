# Write a Python program to convert a list of multiple integers into a single integer
list = [11,22,33,44]
for i in list:
    print(i,end="")

# using list comprehension:
s = [str(i) for i in list]
print("".join(s))