# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK3

# Solution To Question 1(B) : Ex 14, CH 8 - Gas Prices

# Named Constants
START_YEAR = 1993
END_YEAR = 2013
START_MONTH = 1
END_MONTH = 12


def get_Price(string):
    # The foll line will split each element into 2 parts - date & price
    # items[0] will store date & items[1] will store price
    items = string.split(':')
    return float(items[1])

def get_date_number_format(string):
    items = string.split(':')
    date_items=items[0].split('-')
    date_number = int(str(date_items[2]) + str(date_items[0]) +  str(date_items[1]))
    return date_number


def get_Year(string):
    items = string.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])


def get_Month(string):
    items = string.split(':')
    date_items = items[0].split('-')
    return int(date_items[0])

def get_YearMonth(string):
    items = string.split(':')
    date_items = items[0].split('-')
    return  str(date_items[2])+str(date_items[0])


def average_month(G_List, year_month):
    total = 0.0
    count = 0
    avg = 0
    for text in G_List:
        if int(get_YearMonth(text)) == int(year_month):

            total += get_Price(text)
            count += 1
        else:
            continue
        avg = total / count
    if avg>0:

       print('The average gas price in %d' % year_month, ' is $', format(avg, '.2f'), sep='')


def main():
    # Read the contents of the file into a list+
    infile = open('GasPrices.txt', 'r')
    Gas_List = infile.readlines()
    infile.close()

    # Remove \n from every element of the list
    index = 0
    while index < len(Gas_List):
        Gas_List[index] = Gas_List[index].rstrip('\n')
        index += 1

    months_List = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Display the average of the gas prices for each month

    for year in range(START_YEAR, END_YEAR + 1):
        # print('The average gas price in ', months_List[j-1] ,', ', i,' is $', format(average_month(Gas_List,i,j),'.2f'),sep='')
        for month in range( 1,13):
            if len(str(month))==1:
                month = '0'+ str(month)

            year_month = int(str(year) + str(month))
            #print(year_month)
            average_month(Gas_List, year_month)


main()
