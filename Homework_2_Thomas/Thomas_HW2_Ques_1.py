# Tara Ann Thomas 

# INSY5336 - HOMEWORK2

# Solution To Question 1 : Ex 12, CH 4 - Calculating the factorial of a number

# A simple for loop can determine the factorial

num = int(input('Hello! Please enter a  number for which you wish to determine the factorial: '))
factorial = 1 # Stores the factorial of the number that the user inputs.

# Calculating the factorial

for count in range(num,0,-1):
    factorial = factorial * count

print('The factorial of', num, 'is', factorial)
    
