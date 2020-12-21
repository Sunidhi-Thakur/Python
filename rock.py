from random import randint

computer = randint(1,3)
ch = 'y'

while ch == 'y' or ch == 'Y' :
    player = int(input("\nPress 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors\n"))
    if player == computer:
        print("\nTie!")
    elif player == 1:
        if computer == 2:
            print("You lose!")
        else:
            print("You win!")
    elif player == 2:
        if computer == 3:
            print("You lose!")
        else:
            print("You win!")
    elif player == 3:
        if computer == 1:
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid Input")
    
    ch = input("\nReplay? [Y|N]: ")
    if ch == 'N' or ch == 'n':
        break
        
    computer = randint(1,3)