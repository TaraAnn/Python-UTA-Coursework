# Tara Ann Thomas 

# INSY5336 - HOMEWORK1

# Solution To Question 6 : Ex 16 - February Days, CH 3

#Obtain the year from the user.
year = int(input('Hello! Please enter a year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('In', year, "February has 29 days. It's a leap year!")

else:
    if year % 4 == 0:
        print('In', year, "February has 29 days. It's a leap year!")
    else:
        print('In', year, "February has 28 days. It is not a leap year!")




