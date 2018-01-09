# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK3

# Solution To Question 1(C) : Ex 14, CH 8 - Gas Prices


def get_Price(string):
    # The foll line will split each element into 2 parts - date & price
    # items[0] will store date & items[1] will store price
    items = string.split(':')
    return float(items[1])


def sort_gas_price_asc(G_List):
    len_val = len(G_List)
    for i in range(0,len_val):
        for j in range(0, len_val):
         if get_Price(G_List[i])<get_Price(G_List[j]):
             temp= G_List[i]
             G_List[i] = G_List[j]
             G_List[j] = temp
    print("Sorted gas price from lowest to highest:")
    for text in G_List:
        print(text)


def sort_gas_price_dsc(G_List):
    len_val = len(G_List)
    for i in range(0,len_val):
        for j in range(0, len_val):
         if get_Price(G_List[i])>get_Price(G_List[j]):
             temp = G_List[i]
             G_List[i] = G_List[j]
             G_List[j] = temp
    print("Sorted gas price from highest to lowest:")
    for text in G_List:
        print(text)


def main():
    # Read the contents of the file into a list
    infile = open('GasPrices.txt', 'r')
    Gas_List = infile.readlines()
    infile.close()

    # Remove \n from every element of the list
    index = 0
    while index < len(Gas_List):
        Gas_List[index] = Gas_List[index].rstrip('\n')
        index += 1

    # Display the highest gas prices for each year
    sort_gas_price_asc(Gas_List)
    print()
    sort_gas_price_dsc(Gas_List)


main()
