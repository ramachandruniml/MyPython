import random

gamePick = ["rock", "paper", "scissors"]

if __name__ == "__main__":
    pick = random.choice(gamePick)
    print(pick)

    print("Welcome to the Rock, Paper, Scissors game!")
    print("------")
    choice = input("Pick one of the three: rock, paper, or scissors")

    if(pick=="rock"):
        if (choice=="rock"):
            print("You both picked Rock")
            print("Try again. ")
        elif(choice =="paper"):
            