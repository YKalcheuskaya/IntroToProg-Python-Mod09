# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2022,Created started script
# RRoot,1.1.2022,Added pseudo-code to start assignment 9
# YKalch,3.15.2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    import DataClasses as D
    import ProcessingClasses as P
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Data declaration -------------------------------------------------------- #

employees_registry_file = 'EmployeeData.txt'
list_employees = []

# Data declaration -------------------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
file_data = P.FileProcessor.read_data_from_file(employees_registry_file)
for line in file_data:
    list_employees.append(D.Employee(line[0], line[1], line[2].strip()))

# Endless cycle before user exits the program
while True:
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    menu_choice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if menu_choice == '1':
        Eio.print_current_list_items(list_employees)
        continue  # to show the menu

    # Let user add data to the list of employee objects
    elif menu_choice == '2':
        employee = Eio.input_employee_data()
        if employee is not None:
            print("Adding new employee to the list: " + employee.to_string())
            list_employees.append(employee)
        continue  # to show the menu

    # Let user save current data to file
    elif menu_choice == '3':
        P.FileProcessor.save_data_to_file(employees_registry_file, list_employees)
        continue  # to show the menu

    # Let user exit program
    elif menu_choice == '4':
        exit()

    else:
        print("Invalid menu choice! Correct options: [1-4]")

# Main Body of Script  ---------------------------------------------------- #
