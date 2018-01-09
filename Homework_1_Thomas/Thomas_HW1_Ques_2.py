# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 2 : Ex 12 - Software Sales, CH 3

#Named Constants
RETAIL_PRICE = 99.0


#Obtain No. of packages from the user.
packages=int(input('Hello! Please enter the number of packages you wish to purchase: '))

# Calculating Discount
if packages == 0:
    print('You must purchase atleast one package')

elif packages > 0 and packages < 10: # For packages less than 10, no discount is offered.
    discount=0
    sale_price = RETAIL_PRICE - discount 
    print('The discount on your purchase is : $',discount,sep='')
    print('Your payable amount is : $',sale_price,sep='')
    
elif packages >= 10 and packages <= 19: # For packages between 10 to 19, a discount of 10% is offered
    discount = RETAIL_PRICE * 0.1
    sale_price = RETAIL_PRICE - discount
    print('The discount on your purchase is : $',discount,sep='')
    print('Your payable amount is : $',sale_price,sep='')
    
elif packages >= 20 and packages <= 49: # For packages between 20 to 49, a discount of 20% is offered
    discount = RETAIL_PRICE * 0.2
    sale_price = RETAIL_PRICE - discount
    print('The discount on your purchase is : $',discount,sep='')
    print('Your payable amount is : $',sale_price,sep='')
    
elif packages >= 50 and packages <= 99: # For packages between 50 to 99, a discount of 30% is offered
    discount = RETAIL_PRICE * 0.3
    sale_price = RETAIL_PRICE - discount
    print('The discount on your purchase is : $',discount,sep='')
    print('Your payable amount is : $',sale_price,sep='')

elif packages >= 100: # For packages greater than 100, a discount of 40% is offered
    discount = RETAIL_PRICE * 0.4
    sale_price = RETAIL_PRICE - discount
    print('The discount on your purchase is : $',discount,sep='')
    print('Your payable amount is : $',sale_price,sep='')

else:
    print('Please enter a valid input')
