# 1).Single Inheritance:
class Company:
    def policy(self):
        print("policy_name- AXA Life Insurance")
        print("policy_details- grade: B")

class Employee(Company):
    def details(self):
        print("Employee Health Insurance")
        
e = Employee()
e.details()
e.policy()

# 2).Multiple Inheritance:
class Engine:                 # (parent class1)
    def start(self):
        print("Suzuki Swift is an Engine started Car")

class Electric:               # (parent class2)
    def charge(self):
        print("Suzuki Dezire is a Battery charging car")

class HybridCar(Engine, Electric):      # (child class)
    def drive(self):
        print("Suzuki Grand Vitara is a Hybrid car, which has both features of Engine as well as Battery charging")

hybrid = HybridCar()
hybrid.start()
hybrid.charge()
hybrid.drive()

# example-2
# multiple inheritance:
# parent class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# parent class2
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# child class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

# 3).Multilevel Inheritance:
class Grandparent:
    def grandparent_method(self):
        print("Grand father have a Villa")

class Parent(Grandparent):
    def parent_method(self):
        print("father have a Car")

class Child(Parent):
    def child_method(self):
        print("Son have liquid Cash & Ornaments")

child = Child()
child.grandparent_method()
child.parent_method()
child.child_method()

# 4).Hierarchical Inheritance: 

class Mould:        # (one Base class)
    def pattern(self):
        print("Idol Mould for making Ganesha")
class Idol1(Mould):     #(child1)
    def idol_1(self):
        print("Ganesha Idol with Light Grey clour")
class Idol2(Mould):     #(child2)
    def idol_2(self):
        print("Ganesha Idol with Orange & Sky blue clour")
class Idol3(Mould):     #(child3)
    def idol_3(self):
        print("Ganesha Idol with different colours")

# Creating instances of derived classes
idol1 = Idol1()
idol2 = Idol2()
idol3 = Idol3()

# Calling the methods to print the output
idol1.pattern()  
idol1.idol_1()   

idol2.pattern()  
idol2.idol_2()   

idol3.pattern()  
idol3.idol_3()   

