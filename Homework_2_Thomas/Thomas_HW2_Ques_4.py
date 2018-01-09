# Tara Ann Thomas (UTA ID : 1001584535)

# INSY5336 - HOMEWORK2

# Solution To Question 4 : Ex 20, CH 5 - Random Number Guessing Game



import random


def main():
    # initialize
    play_active = True
    attempts =0
    # while game is active
    while play_active == True:
        # increase the turn count for each iteration

        print('Pick a number from 1 to 100 and let\'s see if your guess is correct')
        print('Enter your guess: \n')
        num = input()
        # validate the input provide and check for equality
        if num.isnumeric() == True and int(num)>=1 and int(num)<=100 :
            attempts += 1
            if check_equality(int(num), attempts) == True:
                print('Let\'s play again!')
                play_active = False
                play_again()
        
        else:
            print('Invalid attempt.')





def check_equality(value, turns):
    # ran_no = random.seed(10) # This statement was used only to test the functionality of the code
    ran_no = random.randint(1, 100)
    # Scenario when user input equal to the random number
    if value == ran_no:
        # Acknowledge user about success
        print('Congratulations! You have guessed correctly!')
        print('You took', turns, 'attempts to guess the correct number')
        # Return True when match is found
        return True
    # Scenario when user less than to the random number
    elif value < ran_no:
        print('Too low, try again. The number was', ran_no)
    # Scenario when user greater than to the random number
    elif value > ran_no:
        print('Too high, try again. The number was', ran_no)
    # Return false when match is not found
    return False

def play_again():

    # Ask user to play the game again
    print('Press Y to continue or N to exit:\n')
    play_on = input()
    if play_on == 'N':
        print('Thanks for playing!')
        exit()
    elif play_on == 'Y':
        repeat()
    else:
        print('Sorry wrong input')
        play_again()

def repeat():
    #  call main function again
    main()

# call the main function
main()
