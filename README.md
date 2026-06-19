Employee Management System (EMS)

Objective - Create a simplified Employee Management System (EMS). This project will cover control structures,
functions, and object-oriented programming concepts to manage employee data.

Steps to Implement

Step 1 - Plan the Data Storage
         Use a dictionary to store employee data where the keys is the emp_id (Employee ID) and the value is another dictionary containing:


 name: Employee's name.
age: Employee's age.
department: Employee's department.
salary: Employee's monthly salary.
  Initialize the dictionary with some sample employee data for testing (e.g., {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}).


Step 2 - Define the Menu System
         Create a menu that displays the following options:


 Add Employee
 View All Employees
 Search for Employee
 Exit
 Implement a loop to continuously display the menu until the user chooses to Exit.


Step 3 - Add Employee Functionality
         Prompt the User to enter the following details for a new employee:


 emp_id (Employee ID)
 name (Employee Name)
 age (Employee Age)
 department (Employee Department)
salary (Employee Salary)
 Validate Input: Make sure the Employee ID is unique. If it already exists in the dictionary, ask the user to enter a new ID.


  Store the Employee data in the dictionary using the entered emp_id as the key and the other details as values.


Display a message indicating the employee was successfully added.

Step 5 - Search for an Employee by ID
         Prompt the User to enter the emp_id they want to search for.
         Search the Dictionary:
         If the employee exists, display their details (name, age, department, salary).
         If the employee does not exist, display a message like:
         "Employee not found."


Step 6 - Exit the Program
         Add an Exit option in the menu.
         If the user chooses Exit, display a thank-you message and exit the program

