word = input("enter input:")
word = word.upper()
rev_word = word[::-1]
if word == rev_word:
    print("Palindrome")
else:
    print("Not a Palindrome")
    