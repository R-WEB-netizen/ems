#step 1- Plan the data storage.


employees = {}


#step 3- Add Employee function
def add_Employee(employees):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    
    if emp_id in employees:
        print("Employee already exists!")
    else:
        employees[emp_id] = {"Name": name, "Age": age, "Department": department, "Salary": salary}
        print("Employee added successfully!")
#Step 4 - View All Employees

def view_all_employees(employees):
    if len(employees) == 0:
        print("No employees available.")
    else:
        print("\n{:<10} {:<20} {:<5} {:<15} {:<10}".format(
            "ID", "Name", "Age", "Department", "Salary"))
        print("-" * 65)

        for emp_id, details in employees.items():
            print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
                emp_id,
                details["Name"],
                details["Age"],
                details["Department"],
                details["Salary"]
            ))   

#Step 5 - Search for an Employee by ID

def search_employee(employees):
    emp_id = input("Enter employee ID to search: ")
    if emp_id in employees:
        details = employees[emp_id]
        print(f"Employee found:")
        print(f"ID: {emp_id}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Department: {details['Department']}")
        print(f"Salary: {details['Salary']}")
    else:
        print("Employee not found.")
#Step 6 - Exit the Program

def exit_program():
    print("Thank you for using the Employee Management System. Goodbye!")
    exit()
#step 2- define the menu system
def display_menu():
    print("1.Add Employee")
    print("2.View All Employee")
    print("3.Search for Employee")
    print("4.Exit")

while(True):
    display_menu()

    choice = int(input("choose the option:"))

    if choice == 1:
        print("you choose:",add_Employee(employees))

    elif choice == 2:
           print("you choose:",view_all_employees(employees))

    elif choice == 3:
         print("you choose:",search_employee(employees))


    elif choice == 4:
        print("exit")
        exit_program()

    else:
        print("choose the correct option")

ems = employees()
print(ems)
