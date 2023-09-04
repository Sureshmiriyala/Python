list1 = [input("enter input:")]
 
for num in list1:
   if num % 2 == 0:
       print("even:",num)
    else:
      print("odd:",num)

# using for loop & range :
list=[]
x = int(input("Enter the Starting of the range:"))
y = int(input("Enter the Ending of the range:"))
for i in range(x,y):
  list.append(i)
print("Original Number List:", list)
even_list = []
odd_list = []
for i in range(len(list)):
  if(list[i]%2 == 0):
    even_list.append(list[i])
  else:
    odd_list.append(list[i])
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)

# using for loop:
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,32,43,54,65,66,78,79]
even_list = []
odd_list = []
for i in range(len(list)):
	if list[i] % 2 == 0:
		even_list.append(list[i])
	else:
		odd_list.append(list[i])
    
print("Even list:",even_list)
print("Odd list:",odd_list)