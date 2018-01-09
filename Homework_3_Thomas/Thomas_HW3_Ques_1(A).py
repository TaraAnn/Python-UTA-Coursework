# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK3

# Solution To Question 1(A) : Ex 14, CH 8 - Gas Prices

# Named Constants
START_YEAR = 1993
END_YEAR = 2013

def get_Price(string):
    #The foll line will split each element into 2 parts - date & price
    #items[0] will store date & items[1] will store price
    items = string.split(':')
    return float(items[1])

def get_Year(string):
    items = string.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])

def average_years(G_List,year):
    total = 0.0
    count = 0
    for text in G_List:
        if get_Year(text) == year:        
            total += get_Price(text)
            count+=1
    avg = total/count
    return avg

def main():
    #Read the contents of the file into a list
    infile = open('GasPrices.txt','r')
    Gas_List = infile.readlines()
    infile.close()
    
    #Remove \n from every element of the list
    index = 0
    while index < len(Gas_List):
        Gas_List[index] = Gas_List[index].rstrip('\n')
        index+=1

    #Display the average of the gas prices for each year
    for i in range(START_YEAR,END_YEAR+1):
        print('The average gas price in the year ', i, ' is $', format(average_years(Gas_List,i),'.2f'),sep='')
    

main()
