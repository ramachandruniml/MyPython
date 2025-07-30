import random

gamePick = ["rock", "paper", "scissors"]

if __name__ == "__main__":
    pick = random.choice(gamePick)
    print(pick)

    print("Welcome to the Rock, Paper, Scissors game!")
    print("------")
    points = int(input("How many points do you want to play until?"))
    computer = 0
    player=0
    while (player!=points and computer !=points):
        pick = random.choice(gamePick)
        print("Pick one of the three: rock, paper, or scissors")
        choice = input("Enter your choice: ")
        if(pick=="rock"):
            if (choice=="rock"):
                print("You both picked Rock")
                print("Try again. ")
            elif(choice =="paper"):
                print("The computer picked rock.")
                print("You won!")
                player+=1
            else:
                print("The computer picked rock.")
                print("You lost.")
                computer+=1
        if(pick=="paper"):
            if (choice=="paper"):
                print("You both picked paper")
                print("Try again. ")
            elif(choice =="rock"):
                print("The computer picked paper.")
                print("You lost")
                computer+=1
            else:
                print("The computer picked paper.")
                print("You won!")
                player+=1
        if(pick=="scissors"):
            if (choice=="scissors"):
                print("You both picked scissors")
                print("Try again. ")
            elif(choice =="paper"):
                print("The computer picked scissors.")
                print("You lost")
                computer+=1
            else:
                print("The computer picked scissors.")
                print("You won!")
                player+=1
        print("Player: "+ str(player) +"Computer: "+ str(computer))



    print("These are the final points:")
    print("Player: "+ str(player +"Computer: "+ computer)
    if (player>computer):
        print('You won the game!')
    elif(computer>player):
        print("The computer won and you lost :(")
    elif(computer==player):
        print("The game ended on a tie.")