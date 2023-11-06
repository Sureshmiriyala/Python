# Public Member: Accessible anywhere from outside of the class.
class Employee:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
    
    # public instance method
    def display(self):
        print("Name: ",self.name,"Designation: ",self.designation)

e = Employee("Suresh","Developer")                      # creating object of a class
print("Name: ",e.name,"Designation: ",e.designation)    # accessing public data members
e.display()                                             # calling public method of a class


# Private members are Accessible only within the class and we can’t access them directly from the class objects.
# Private Member: We can protect variables in the class by marking them private
class Employee:
    def __init__(self,name,designation):
        self.name = name
        self.__designation = designation
    
    # public instance method
    def display(self):
        # private members are accessible from a class
        print("Name: ",self.name,"Designation: ",self.__designation)

e = Employee("Suresh","Developer")                      # creating object of a class
# print("Name: ",e.name,"Designation: ",e.designation)   we can’t access the private variable from the outside of that class.
e.display() 
# To Access the Private member
print("Designation: ",e._Employee__designation) # direct access to private member using name mangling

# Note: We can directly access private and protected variables from outside of a class through name mangling.






