def Add_Employee():
 
    email_Id = input("Enter Employee emial_Id : ")
 
    if(email_Id) == True:
        print("Employee already exists")
        
    else:
        Id = input("Enter Employee Id : ")
        Name = input("Enter Employee Name : ")
        Domain = input("Enter Employee Domain : ")
        Salary = input("Enter Employee Salary : ")

Add_Employee()

# Method-2 (using add fun(), remove() & check)
emp = {}
def add_emp():
    name = input("enter the emp name: ")
    emp_id = input("enter the emp id: ")
    domain = input("enter the domain: ")
    email_id = input("enter the emial id: ")
    emp[name] = {"emp_id":emp_id,"domain":domain,"email_id":email_id}
    print("emp details added successfully")

def get_emp_details_by_compare_with_email_id():
    email_id = input("enter the email id to compare: ")
    found = False
    for key,values in emp.items():
        if(value["emp_id"] == emp_id):
            print(f"{key}:{value}")
            found = True
        if not found:
            print("no employees are found with email id : ")

def remove_particular_employee():
    name_to_be_remove = input("enter the name of the employee to be remove: ")
    if (name_to_be_remove in emp):
        del emp[name_to_be_remove]
        print(f"{name_to_be_remove} is remove from the list.")
    else:
        print(f"not found with employee name of {name_to_be_remove}")

No_of_employees = int(input("enter the no of employees:"))
for i in range(No_of_employees):
    add_emp()

print(emp)
get_emp_details_by_compare_with_email_id()
remove_particular_employee()


# Method-3

employ_details={
    101:{"Name":"Suresh","Domain":"Python","Emp_id":"MT-01968","Mail":"suresh123.marolix@gmail.com"},
    102:{"Name":"kiran","Domain":"Python","Emp_id":"MT-01967","Mail":"kiran.marolix@gmail.com"},
    103:{"Name":"Ravi Mishra","Domain":"Python","Emp_id":"MT-01978","Mail":"ravi_mishra.marolix@gmail.com"},
    104:{"Name":"lavanya","Domain":"Devops","Emp_id":"MT-01826","Mail":"lavanya1233.marolix@gmail.com"}
}

check_the_input=input("the value is remove or update or add or check:")

if check_the_input=="check":
    given_empId=int(input("enter empId:"))
    if given_empId in employ_details:
        print(employ_details[given_empId])
    else:
        print("Employee Id Is Not Found")
elif check_the_input=="add":
    add_key=int(input("enter empId:"))
    employee=eval(input("enter emp Dtails:"))
    employ_details[add_key]=employee
    print(employ_details)
    print(employ_details[add_key])
    print(len(employ_details))
elif check_the_input=="update":
    given_empId=int(input("enter empId:"))
    given_key=input("enter the key:")
    update_value=input("enter the val:")
    if given_empId in employ_details:
        employ_details[given_empId][given_key]=update_value
        print(employ_details[given_empId])
    else:
        print("Not Found the Employee Id")
elif check_the_input=="remove":
    given_empId=int(input("enter the empId:"))
    if given_empId in employ_details:
        employ_details.pop(given_empId)
        print(employ_details)
    else:
        print("Not Found The Employee Id")
else:
    print("Enter The Correct Employee Id")