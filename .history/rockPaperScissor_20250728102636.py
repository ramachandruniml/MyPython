import random

gamePick = ["Rock", "Paper", "Scissors"]

if __name__ == "__main__":
    pick = random.choice(gamePick)
    print(pick)

    print("Welcome to the Rock, Paper, Scissors game!")
    print("------")
    choice = input("Pick one of the three: Rock, Paper, or Scissors")

    if(pick=="Rock"):
        
