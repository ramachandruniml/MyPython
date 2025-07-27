import random 
from collections import Counter
words = ["banana", "apple", "strawberry", "blueberry", "raspberry", "orange", "cherry", "grapes", "passionfruit", "watermelon"]

if __name__== '__main__':
    fruit = random.choice(words)
    letterGuess = ''
    falseLetterGuess = ' '
    correct=0
    end=0
    for x in fruit:
        print('_', end=' ')
    print()

    numGuesses = len(fruit)+2
    
    while numGuesses !=0 and end==0: 
        guess = input("You have " + str(numGuesses) + " Guesses left. Guess a letter: ")
        

        if (guess.isalpha()==True):

            if guess in letterGuess or guess in falseLetterGuess:
                print('You have already guessed this letter.')
            else: 
                numGuesses -=1 
                if guess in fruit:
                    
                    occurence = fruit.count(guess)
                    for _ in range(occurence):
                        letterGuess += guess

                    print("Your guess is correct")

                    for x in fruit:
                        if x in letterGuess and (len(letterGuess) != len(fruit)):
                            print(x, end=' ')
                            correct+=1

                        elif((len(letterGuess))==(len(fruit))):
                            end=1
                            print("The word is: ", end = ' ')
                            print(fruit)
                            flag=1
                            print("Congratulations you won!")
                            break 
                            
                            
                        else:
                            print('_', end=' ')
                    print()
                    
                else:

                    falseLetterGuess+= guess
                    print("The letter you guessed is not in the word.")

        else:
            print("Please enter a letter. ")
        if end==1:
            break
    if numGuesses==0 and (len(letterGuess)!=len(fruit)):
        print("-----------------------")
        print("You ran out of guesses.")
        print("You lost :(")
        print("The word was: " + fruit)
        print("-----------------------")