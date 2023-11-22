# # reverse the number:
# num = int(input("enter the numbers:"))
# rev = int(str(num)[::-1])
# print(rev)

# num = int(input("enter the numbers:"))
# x = [int(i) for i in str(num)]
# x.reverse()
# print(x)

# num = input("enter the input:")
# x = ""
# for i in range(len(num)-1,-1,-1):
#     x = x + num[i]
# print(x)

# # Checking the given number is an Armstrong number or not:

# num = int(input("enter the number:"))
# num_str = str(num)
# length = len(num_str)
# sum = 0
# for digit in num_str:
#     sum = sum + int(digit)**length
# if sum == num:
#     print(num,"is an armstrong number")
# else:
#     print(num,"is not an armstrong number")

# # deleting the pair from a dictionary:
# dict= {'a':10,'b':20,'c':30}
# dict.pop('b')
# print(dict)

# d= {'a':10,'b':20,'c':30}
# del d['b']
# print("d= ",d)

# # Check wether a Palindrome or not:
# string = input("enter a string:")
# string_lower = string.lower()
# rev_string = string_lower[::-1]

# if rev_string == string_lower:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# checking Anogram:
str1 = input("enter string1:")
str2 = input("enter a string2:")

str1_lower = str1.lower()
str2_lower = str2.lower()

if len(str1)==len(str2):
    str1_sort = sorted(str1)
    str2_sort = sorted(str2)

    if str1_sort == str2_sort:
        print("Anogram")
    else:
        print("Not an Anogram")

