#This program will ask the user for a file name and use the data given to calcualte the total pay 
# of an employee given their last name, hours wokred and wages

#prompt the user for the file name
file_name = input("What is the name of yuor file?")

#open the file for reading
with open(file_name, 'r') as file:
#read all the lines and save them in employees list
        employees = file.readlines()
        #initialize a list named data
data=[]
#use a for loop to go through the list of lines and split them and
# assign them to crrect variables such as last name, hours worked, and wages
for employee in employees:
    last_name, hours, wage = employee.split()
    total_amount=float(hours)*float(wage)
    data.append([last_name, hours, f'{total_amount:.2f}'])
#print the top of the table with correct spacing
table_format = f"{'Name':<15}{'Hours':<10}{'Total Pay'}\n"
#use a for loop to go through the list data and make the table name, hours,
# and total pay of the employee with correct spacing
for employee in data:
    table_format += f"{employee[0]:<15}{employee[1]:<10}{employee[2]}\n"

#print the table
print(table_format)
        



