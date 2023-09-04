# id() func by using diffrent variables
a = 3 
b = 8 
c = 12.6
txt = "hello"
str = "hello"

#print(id(a))
#print(id(b))
#print(id(c))
#print(id(txt))
#print(id(str))

# by using list
list1 = [1,2,3,4]                    # In case of lists, 
list2 = [1,2,3,4]                           # list1 & list2 are not same id's
list3 = ['A','B','C','D']                       # similarly, list3 & list4 are not same id's
list4 = ['A','B','C','D']

#print(id(list1))
#print(id(list2))
#print(id(list3))
#print(id(list4))

# by using tuples
tuple1 = (1,2,3,4)                  # Here, tuple1 are tuple2 are getting same id's
tuple2 = (1,2,3,4)
tuple3 = ('A','B','C','D')          # Here, tuple3 are tuple4 are getting same id's
tuple4 = ('A','B','C','D')
#print(id(tuple1))
#print(id(tuple2))
#print(id(tuple3))
#print(id(tuple4))

# using sort() function
string = "Python Batch"
new_list = []

for char in string:
    new_list.append(char)
print(new_list)
new_list.sort()
print(new_list)

# insert() function 
python_batch = ["ram","amar","Lucky","anoop"]
python_batch.insert(2,"kiran")
print(python_batch)

# pop() function 
x = [1,2,3,4,6,5,6,7,8]
x.pop(4)
print(x)

# slicing()
l = [1,2,3,4,5,6,7,8,9,10]
print(l[1:10:2])

# get() function
d={1:"sai",2:"harshini",3:"suresh"}
print(d)
print(type(d))
print(d[1])
print(d.get(1))

s = "Kiran"
print(s.max())
print(s.min())



    