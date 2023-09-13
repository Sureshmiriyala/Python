l1 = ["small", "big"]
l2 = ["book", "chair", "table"]

for x in l1:
  for y in l2:
    print(x, y)

# printing the string using nested loop 3* 2 times:
for i in range(3):
    for j in range(2):
	    print("Hello World")

# printing star pattern using nested loop:
rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')