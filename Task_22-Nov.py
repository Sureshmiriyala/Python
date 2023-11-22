# # Checking prime or not:
# n = int(input("enter a number to check:"))
# count = 0
# if n > 2:
#     for i in range(2,n):
#         if n%i ==0:
#             count = 1
#             break
# if count ==1:
#     print("Not a Prime Number")
# else:
#     print("Prime Number")

# # To Print Fibonacci Series:
# nterms = int(input("Enter the required nterms:"))
# n1,n2 = 0,1

# print("Fibonacci Series:",n1,n2,end=" ")
# for i in range(2,nterms):
#     n = n1+n2
#     n1= n2
#     n2= n
#     print(n,end=" ")

# #To Remove a specified character from a string:
# string = input("enter the string:")
# character = input("enter a character to remove from the string:")
# new_string = string.replace(character,"")
# print(new_string)

# string = input("enter a string:")
# result = (set(string))
# print(result)

# # To print the duplicate characters in the string:
# string = input("enter a string:")
# new_string = ''.join([char for char in string if string.count(char)>1])
# print(new_string)

# # To remove the Duplicate characters from the string:
# str = input("enter string:")
# unique_str = []

# for char in str:
#     if char not in unique_str:
#         unique_str.append(char)

# result = ''.join(unique_str)
# print(result)

# # method-2
# str = input("enter the string:")
# new_str =""

# for char in str:
#     if char not in new_str:
#         new_str = new_str+char
# print(new_str)

# # To check the given char is vowel or not:
# char = input("enter a character to be check:")
# sub_string = "AEIOUaeiou"

# if char in sub_string:
#     print("Given Character is a vowel")
# else:
#     print("Is not a vowel")

# # To count the occurance of the given char from a string:
# word = input("enter a word:")
# char = input("enter the character to check:")
# result = word.count(char)
# print(result)


# # To find the sum of integers in the string:
# string = input("enter a string:")
# sum = 0
# for char in string:
#     if char.isdigit():
#         sum = sum+int(char)
# print(sum)

# # Replace string space with given character:
# string = input("enter a string:")
# chr = input("enter a replace character:")
# result = ""

# for char in string:
#     if char==" ":
#         char = chr
#     result = result + char
# print(result)

# # To convert lowercase character to uppercase character of string:
# str = input("enter a string:")
# result = ""

# for i in str:
#     if i.islower():
#         i = i.upper()
#     result = result + i
# print(result)

# # To Convert Lowercase vowels to Uppercase
# string = input("enter the word:")
# vowels = "aeiou"

# for char in string:
#     if char in vowels:
#         char_upper = char.upper()
#         string = string.replace(char,char_upper)
# print(string)

# # to remove the vowels from a string:
# string = input("enter the string:")
# new_string = ""

# for i in string:
#     if i not in "aeiou":
#         new_string = new_string + i
# print(new_string)

# # To count vowels and consonants in the string:
# string = input("enter a string:")
# vowels = 0
# consonants = 0

# for char in string:
#     if char in "aeiou":
#         vowels = vowels + 1
#     elif char.isalpha():
#         consonants = consonants + 1
# print("Vowels count: ",vowels)
# print("Consonants count: ",consonants)
        
# print the character with the highest frequency in a string:
string = input("enter the input:")
max_char = ""
max_frequeny = 0

for char in string:
    frequency = string.count(char)

    if frequency > max_frequeny:
        max_char = char
        max_frequeny = frequency

print("highest frequency: ",max_char)
print("Count of char: ",max_frequeny)









