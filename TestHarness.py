# ---------------------------------------------------------- #
# Title: Test Harness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2022,Created started script
# YKalch,3.15.2022,Added more tests for different modules
# YKalch,3.15.2022,Reformatted the module in PyCharm
# ---------------------------------------------------------- #

if __name__ == "__main__":
    import DataClasses as D
    import ProcessingClasses as P
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test Data classes
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")

lstPersons = [objP1, objP2]
for person in lstPersons:
    print(person.to_string(), type(person))

objE1 = D.Employee(1, "John", "Sallivan")
objE2 = D.Employee(2, "Yuliya", "Kalcheuskaya")

lstEmployees = [objE1, objE2]
for employee in lstEmployees:
    print(employee.to_string(), type(employee))

# Test Processing classes
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstEmployees)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstEmployees.clear()

for line in lstFileData:
    lstEmployees.append(D.Employee(line[0], line[1], line[2].strip()))

for employee in lstEmployees:
    print(employee.to_string(), type(employee))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstEmployees)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
