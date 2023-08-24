string = input("enter input:")
space = ""
replace_with = input("enter char:")
for i in string:
    if i == " ":
        i = replace_with
    space += i
print(space)