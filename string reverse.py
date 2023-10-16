string = input("Enter input: ")
words = string.split()
reverse = " ".join(reversed(words))
print(reverse)
print(string[::-1])

reverse_of = [word[::-1]for word in words]
print(reverse_of)
reverse_of_string = " ".join(reverse_of)
print(reverse_of_string)
