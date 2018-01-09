# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK3

# Solution To Question 1(C) : Ex 14, CH 8 - Gas Prices

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

def get_date(string):
    items = string.split(':')
    return items[0]

def highest_price(G_List,year):
    max_price = 0.0
    for text in G_List:
        if get_Year(text) == year:        
            price = get_Price(text)
            if price > max_price:
                max_price = price
                date = get_date(text)
    return max_price, date

def lowest_price(G_List,year):
    min_price = 5.0
    for text in G_List:
        if get_Year(text) == year:        
            price = get_Price(text)
            if price < min_price:
                min_price = price
                date = get_date(text)
    return min_price, date

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

    #Display the highest gas prices for each year
    print('The Highest Gas Prices Per Year:')
    for i in range(START_YEAR,END_YEAR+1):
        maximum_price, max_date = highest_price(Gas_List,i)
        print('The highest gas price in ', i, ' was $', format(maximum_price,'.2f'), ' on ', max_date,sep='')

    print()
    
    #Display the lowest gas prices for each year
    print('The Lowest Gas Prices Per Year:')
    for i in range(START_YEAR,END_YEAR+1):
        minimum_price, min_date = lowest_price(Gas_List,i)
        print('The lowest gas price in ', i, ' was $', format(minimum_price,'.2f'), ' on ', min_date,sep='')
    
main()
