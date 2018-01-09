# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 7 : Ex 17 - WIFI Diagnostic Tree, CH 3

#Named Constants
Sec_In_Min = 60
Sec_In_Hr = 3600
Sec_In_Day = 86400

#Display Message to the user
print("Hello! We understand that you are experiencing \n"+\
      "technical issues with your wifi connection.\n"+\
      "Please follow the steps as instructed.")

print("\nReboot the computer and try to connect.")
response = input("Did that fix the problem(Yes/No)?: ")

if response == 'yes' or response == 'Yes' or response == 'YES':
    print('\nYou have rectified your issue.')
elif response == 'no' or response == 'No' or response == 'NO':
    print("\nReboot the router and try to connect.")
    response = input("Did that fix the problem(Yes/No)?: ")
    if response == 'yes' or response == 'Yes' or response == 'YES':
        print('\nYou have rectified your issue.')
    elif response == 'no' or response == 'No' or response == 'NO':
        print("\nMake sure the cables between the router and modem are plugged firmly.")
        response = input("Did that fix the problem(Yes/No)?: ")
        if response == 'yes' or response == 'Yes' or response == 'YES':
            print('\nYou have rectified your issue.')
        elif response == 'no' or response == 'No' or response == 'NO':
            print("\nMove the router to a new location and try to connect.")
            response = input("Did that fix the problem(Yes/No)?: ")
            if response == 'yes' or response == 'Yes' or response == 'YES':
                print('\nYou have rectified your issue.')
            elif response == 'no' or response == 'No' or response == 'NO':
                print("\nSorry. You need to get a new router.")
    




