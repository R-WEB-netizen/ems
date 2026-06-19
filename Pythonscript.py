#step 1- Plan the data storage.

employees = {}


#step 3- Add Employee function
def add_Employee(employees):
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    #Prevent duplicate employee IDs
    if emp_id in employees:
        print("Employee already exists!")
    else:
        employees[emp_id] = {"Name": name, "Age": age, "Department": department, "Salary": salary}
        print("Employee added successfully!")
#Step 4 - View All Employees in a table-like structure
#Display all employees stored in the dictionary.

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

#Step 5 - Search  an Employee by ID

def search_employee(employees):
    emp_id = int(input("Enter employee ID to search: "))
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
    print("Thank you for using the EMS. Goodbye!")
    exit()
#step 2- define the menu system
def display_menu():
    print("\n1.Add Employee")
    print("2.View All Employee")
    print("3.Search for Employee")
    print("4.Exit")

#main loop to run the program
while(True):
    display_menu()
    try:
        choice = int(input("choose the option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_Employee(employees)

    elif choice == 2:
           view_all_employees(employees)

    elif choice == 3:
         search_employee(employees)


    elif choice == 4:
        exit_program()
        

    else:
        print("Invalid option. Please choose 1-4.")



