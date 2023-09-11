# checking palindrome using recursion function:
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

# # print the fibonacci using recursion:
def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-2) + fib(i-1)
print(fib(9))

# printing star pattern by using recursion function:
def pattern(num):                       # defining the function
    if num == 0:
        return
    else:
        pattern(num-1)
        print("* "*num)

num = int(input("no of rows:"))
pattern(num)                             # calling function