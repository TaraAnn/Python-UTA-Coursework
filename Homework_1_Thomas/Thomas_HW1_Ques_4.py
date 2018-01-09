# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 4 : Ex 14 - Body Mass Index, CH 3


#Obtain the user's weight.
weight=float(input('Hello! Please enter your weight(in pounds): '))
while weight<=0.0 : # Validation Loop
    print('Please enter a valid weight')
    weight=float(input('Please enter a valid weight(in pounds): '))

#Obtain the user's height.
height=float(input('Hello! Please enter your height(in inches): '))
while height<=0.0 : # Validation Loop
    print('Please enter a valid height')
    height=float(input('Please enter a valid height(in inches): '))

# Calculating BMI
BMIndex = weight*703/height**2

# Optimal Weight
if BMIndex >= 18.5 and BMIndex <= 25: 
    print('Congratulations! Your weight is optimal.' )
else:
    if BMIndex < 18.5: # Underweight
        print('You are underweight.' )
    else: # Overweight
        print('You are overweight.')
