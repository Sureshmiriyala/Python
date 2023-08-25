#count of string
string = input("enter input:")
alpha_count = 0
digit_count = 0
spcl_char_count = 0 

for i in string:
    if i.isalpha():
        alpha_count = alpha_count + 1
    elif i.isdigit():
        digit_count = digit_count + 1 
    else:
        spcl_char_count = spcl_char_count + 1

print("Alpha count is : ",alpha_count)
print("Digit count is : ",digit_count)
print("Special char count is : ",spcl_char_count)