# Tara Ann Thomas 

# INSY5336 - HOMEWORK1

# Solution To Question 3 : Ex 13 - Shipping Charges, CH 3


#Obtain Weight of the package from the user.
package_weight=float(input('Hello! Please enter the weight(in pounds) of the package you wish to ship: '))

# Calculating Shipment Cost

# For packages weighing less than 2 pounds, the rate per pound is $1.50.
if package_weight > 0 and package_weight <= 2: 
    shipping_charges = package_weight * 1.50 
    print('The shipping charges incurred will be : $',format(shipping_charges,'.2f'),sep='')

# For packages weighing between 2 to 6 pounds, the rate per pound is $3.00.    
elif package_weight > 2 and package_weight <= 6: 
    shipping_charges = package_weight * 3.00 
    print('The shipping charges incurred will be : $',format(shipping_charges,'.2f'),sep='')
    
# For packages weighing between 6 to 10 pounds, the rate per pound is $4.00.
elif package_weight > 6 and package_weight <= 10: 
    shipping_charges = package_weight * 4.00 
    print('The shipping charges incurred will be : $',format(shipping_charges,'.2f'),sep='')
    
# For packages weighing greater than 10 pounds, the rate per pound is $4.75.00.
elif package_weight > 10: 
    shipping_charges = package_weight * 4.75 
    print('The shipping charges incurred will be : $',format(shipping_charges,'.2f'),sep='')

else:
    print('Please enter a valid input')
