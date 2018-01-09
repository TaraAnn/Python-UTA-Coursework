# This program manages employee details.
import employee
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'employees.dat'

# main function
def main():
    # Load the existing contact dictionary and
    # assign it to myemployees.
    myemployees = load_employees()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(myemployees)
        elif choice == ADD:
            add(myemployees)
        elif choice == CHANGE:
            change(myemployees)
        elif choice == DELETE:
            delete(myemployees)

    # Save the myemployees dictionary to a file.
    save_employees(myemployees)

def load_employees():
    try:
        # Open the employees.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the employees.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}

    # Return the dictionary.
    return employee_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee\'s details')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up an item in the
# specified dictionary.
def look_up(myemployees):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(myemployees.get(name, 'That name is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add(myemployees):
    # Get the contact info.
    name = input('Name: ')
    idno = input('ID No.: ')
    dept = input('Department: ')
    job = input('Job Title: ')

    # Create an Employee object named entry.
    entry = employee.Employee(name, idno, dept, job)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in myemployees:
        myemployees[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

# The change function changes an existing
# entry in the specified dictionary.
def change(myemployees):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in myemployees:
        # Get a new ID No.
        idno = input('Enter the new ID No.: ')

        # Get a new department.
        dept = input('Enter the new department: ')

        # Get a new Job title.
        job = input('Enter the new job title: ')

        # Create a Employee object named entry.
        entry = employee.Employee(name, idno, dept, job)

        # Update the entry.
        myemployees[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# specified dictionary.
def delete(myemployees):
    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in myemployees:
        del myemployees[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

# The save_employees funtion pickles the specified
# object and saves it to the contacts file.
def save_employees(myemployees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myemployees, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()

    
