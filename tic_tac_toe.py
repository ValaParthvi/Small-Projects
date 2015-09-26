#The Code is written in python3.4.3

from random import randint
from time import sleep


global original_list
original_list = [" " for x in range(9)]     #list to help us show the board


def Choice():       #function to get input from user to select symbol
    global user_symbol

    user_symbol = input("What do you choose? Zero '0' or Cross 'X'?  ") #user selects the symbol
    user_symbol = user_symbol.upper()   #coverting to uppercase,to maitain the flow of program

    if user_symbol not in 'X0O':        #if wrong symbol is entered, user is prompted again to select the symbol
        user_symbol = input("Please choose from '0' or 'X'  .")
    else:   #if user entered correct input, it will just pass
        pass


def Assign_symbol():            #function to assign symbol to machine
    global machine_symbol

    if(user_symbol == 'X'):     #alternative symbol is assigned to machine
        machine_symbol = '0'
    else:                       #if user_symbol is '0', machine will be assigned 'X'
        machine_symbol = 'X'


def first_turn():               #function to select which user will go first
    global first_turn_var
    first_turn_var = randint(0,1)   #randomly selecting the first user to go

    if first_turn_var==0:
        return True                #if True, user will go first
    else:
        return False               #else,if False, machine will go first


def person():   #function to help user input in the desired place in the board
    place_user = int(input("What place? Select from (0-8)"))    #user is prompted to select a place

    if(original_list[place_user]==" "):         #if the entered place is empty,i.e." ",that place will be replaced by user_symbol
        original_list[place_user] = user_symbol
    else:       #if the entered place is already occupied, user will be prompted to enter place again
        print("The place is already occupied.Please enter a place again. ")
        person()


def machine():  #function to let machine input in the randomly generated place in the board
    place_machine = randint(0,8)    #machine will randomly select a place to enter it's symbol

    if(original_list[place_machine] == " "):    #if place is empty, ie." ",replace it with machine symbol
        original_list[place_machine] = machine_symbol
    else:   #if the generated place is already occupied, machine will be asked again to generate the place
        machine()


def Board():        #the board which will be shown to the user
    print('   |   |')
    print(' ' + original_list[0] + ' | ' + original_list[1] + ' | ' + original_list[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + original_list[3] + ' | ' + original_list[4] + ' | ' + original_list[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + original_list[6] + ' | ' + original_list[7] + ' | ' + original_list[8])
    print('   |   |')
    print("\n")

def Winner_Loser():     #this function will decide if a user or machine is winning or losing, or is it a tie.

    if((original_list[0]==machine_symbol and original_list[1] == machine_symbol and original_list[2]== machine_symbol)or\
        (original_list[3]==machine_symbol and original_list[4] == machine_symbol and original_list[5]== machine_symbol)or\
        (original_list[6]==machine_symbol and original_list[7] == machine_symbol and original_list[8]== machine_symbol)or\
        (original_list[0]==machine_symbol and original_list[4] == machine_symbol and original_list[8]== machine_symbol)or\
        (original_list[2]==machine_symbol and original_list[4] == machine_symbol and original_list[6]== machine_symbol)or\
        (original_list[0]==machine_symbol and original_list[3] == machine_symbol and original_list[6]== machine_symbol)or\
        (original_list[1]==machine_symbol and original_list[4] == machine_symbol and original_list[7]== machine_symbol)or\
        (original_list[2]==machine_symbol and original_list[5] == machine_symbol and original_list[8]== machine_symbol)):
        print("Sorry! You lose. Machine Wins!")
        quit()  #program will terminate

    elif((original_list[0]==user_symbol and original_list[1] == user_symbol and original_list[2]== user_symbol)or\
        (original_list[3]==user_symbol and original_list[4] == user_symbol and original_list[5]== user_symbol)or\
        (original_list[6]==user_symbol and original_list[7] == user_symbol and original_list[8]== user_symbol)or\
        (original_list[0]==user_symbol and original_list[4] == user_symbol and original_list[8]== user_symbol)or\
        (original_list[2]==user_symbol and original_list[4] == user_symbol and original_list[6]== user_symbol)or\
        (original_list[0]==user_symbol and original_list[3] == user_symbol and original_list[6]== user_symbol)or\
        (original_list[1]==user_symbol and original_list[4] == user_symbol and original_list[7]== user_symbol)or\
        (original_list[2]==user_symbol and original_list[5] == user_symbol and original_list[8]== user_symbol)):
        print("Bravo! You win!")
        quit() #program will terminate

    else:
        if(" " not in original_list):   #if there is no empty place in the board, then it will be declared as a tie.
            print("It's a tie!")
            quit() #program will terminate
        else:   #else, it will just pass
            pass


def main():     #this function will help us to integrate all the functions defined above
    Choice()                        #user will be asked to choose a symbol
    Assign_symbol()                 #machine will be assigned a symbol,corresponding to user_symbol
    return_value = first_turn()     #first_turn() will decide who will go first, and the return value of first_turn() will be stored in return_value

    for i in range(9):             #for loop will run 9 times(length of the list)
        if(return_value == True):   #return_value is True,so user goes first
            print("Your turn:")

            person()                #person() is called, to let user input a place, to enter user_symbol
            Board()                 #board is printed,to show the progress of the game
            Winner_Loser()          #checking if user or machine is winning or losing

            return_value = False    #return_value is made False, so that the next time loop runs, machine will have the next turn

        else:       #return_value was False, so machine will go first
            print("The machine is thinking...")
            sleep(.7)               #system will sleep for 0.7seconds,a slight break, to think!.

            machine()               #machine() is called, to generate a random place, and enter machine_symbol in that place
            Board()                 #board is printed,to show the progress of the game
            Winner_Loser()          #checking if user or machine is winning or losing

            return_value = True     #return_value is made True, so in the next loop, user will get turn
#return_value is used, so that user and machine can get alternative turns, if user got first turn, machine  can go next, and after that again user, and so on.

if __name__ == '__main__':
    main()
