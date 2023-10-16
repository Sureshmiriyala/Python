# def is_leap(year):
#     leap = False
    
#     if (year%4==0 and year%100 !=0) or(year%400==0):
#         leap = True
    
#     return leap

# year = int(input())
# print(is_leap(year))

# Input the distance in kilometers
distance = float(input("Enter the distance in kilometers: "))

# Initialize the score and bonus_score variables to 0
score = 0
bonus_score = 0

# Check the distance and calculate the score
if distance <= 20:
    score = 2
elif distance <= 60:
    score = 4
else:
    score = 6

# Calculate the bonus score if applicable
if distance > 60:
    bonus_score = 30

# Calculate the total score by adding the score and bonus_score
total_score = score + bonus_score

# Display the score
print(total_score)
