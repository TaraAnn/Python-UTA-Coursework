# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK1

# Solution To Question 5 : Ex 15 - Time Calculator, CH 3
time = int(input('Hello! Please enter the time in seconds\n'))
seconds_1 = time%60
minutes_1 = time//60
hours_1 = minutes_1//60
minutes_1 = minutes_1%60
days_1 = hours_1//24
hours_1 = hours_1%24

if (minutes_1==0) and hours_1==0 and days_1==0:
    print('time in seconds',seconds_1)
elif hours_1==0 and days_1==0:
    print ('time in minutes:',minutes_1,'seconds:',seconds_1)
elif days_1==0:
    print ('time in hours:',hours_1, 'minutes:', minutes_1, 'seconds:',seconds_1)
else:
    print ('time in days:',days_1,'hours:',hours_1,'minutes:',minutes_1,'seconds:',seconds_1)






