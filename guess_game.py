#This is a guess game

import random

print("Hello, what is your name?")

#Get the Name of the player
player = input()
print("Lets Play, " + player)
print("I am thinking of a random integer between 1 and 20")
print("Can you guess correctly in 5 attempts")

#SecretNumber
secretNumber = random.randint(1,20)
print(".....Take a guess......")

print("DEBUGGER: the secret number is " + str(secretNumber))

for guessTaken in range(1,6):
    try:
        guess = int(input())
        if guess < secretNumber:
            print("Your guess is low")
            print("take another guess")
        elif guess > secretNumber:
            print("Your guess is high")
            print("take another guess")
        else:
            break #this condition is for correct guess
    except ValueError:
        print("you did not enter an integer")

if guess == secretNumber:
    if guessTaken == 1:
        print("Good Job! "+ player + " you guessed my number in " + str(guessTaken) + " guess")
    else:
        print("Good Job! "+ player + " you guessed my number in " + str(guessTaken) + " guesses")

    
else:
    print("Oops!, the number I was thinking of was " + str(secretNumber))
