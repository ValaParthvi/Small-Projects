import random

def game():

    l = ['Ross','Rachel','Phoebe','Monica','Chandler','Joey','SmellyCat',\
        'Gunther','CentralPerk','Unagi','SalmonSkinRoll'\
        'FRIENDS','Mike','Barry','Dave','Richard','Emily',\
        'Carol','Susan','Emma','Ben','DaysOfOurLife','FrankJr','Alice','Kathy','Janice']
    friends = [x.upper() for x in l]

    word = random.choice(friends)   #selects a random element from the list friends
    wrong = 0       #keeps track of number of wrong attempts
    attempts = []   #list of wrongly guessed characters
    successful_inputs = []      #list of correctly guessed characters

    print_word = [' _ ' for x in word]  
    print(''.join(print_word)) #prints the empty string

    while(wrong<7):  #loop runs till the user loses all 7 chances or if a break statement is encountered

        user_input = input("Guess the character: ")
        user_input = user_input.upper()
#converting the user_input to uppercase letters to maitain a smooth flow throughout the program

        if(user_input in word):
            if(user_input not in successful_inputs):
                successful_inputs.append(user_input) #keeping track of correctly guessed user_input

                i =0
                while i<len(word):
                    #loop to ensure that the user_input is correctly printed
                    if(user_input==word[i]):
                        print_word[i]= user_input   #replacing '_' with the correctly guessed user_input
                        i+=1    #increamenting the operator
                    else:
                        i+=1
                print(''.join(print_word))
                #printing the string of correctly guessed user_input

        else:   #user_input not in word
            if(user_input not in attempts):
                attempts.append(user_input)
#appending wrongly guessed character(ie user_input) to the list(ie attempts)
                print("Sorry wrong guess!")
                wrong +=1
                if(wrong==1):
                    print('  ______')
                    print(' |      |')
                    print(' |      O')
                    print(' |')
                    print('___')
                    print("6 turns left!")
                if(wrong==2):
                    print('  ______')
                    print(' |     |')
                    print(' |     O')
                    print(' |     |')
                    print('___')
                    print("5 turns left!")

                if(wrong==3):
                    print('  _____')
                    print(' |     |')
                    print(' |     O')
                    print(' |    \|')
                    print(' |')
                    print('___')
                    print("4 turns left!")
                if(wrong==4):
                    print('  ______')
                    print(' |      |')
                    print(' |     O')
                    print(' |    \|/')
                    print(' |')
                    print('___')
                    print("3 turns left!")

                if(wrong==5):
                    print('  ______')
                    print(' |      |')
                    print(' |      O')
                    print(' |     \|/')
                    print(' |      |')
                    print('___')
                    print("2 turns left!")
                if(wrong==6):
                    print('  ______')
                    print(' |      |')
                    print(' |     O')
                    print(' |    \|/')
                    print(' |     |  ')
                    print('___   /')
                    print('Only 1 turn left!')
                if(wrong ==7):
                    print('  ______')
                    print(' |      |')
                    print(' |     O')
                    print(' |    \|/')
                    print(' |     | ')
                    print('___   / \ ')
                    print("All turns are over! Game Over!")
                    print("The word was ",word)

            else:   #user_input not in word and in attempts, ie already guessed and wrong
                print("You already guessed that one!")
        if(''.join(print_word)==word):
#if guessed the whole word correctly, prints the msg and breaks out of the loop.
            print("Congratulations,you guessed it well! Come Play Again.")
            break

def main():
    game()

if __name__ == '__main__':
    main()
