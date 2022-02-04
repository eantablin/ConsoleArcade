import os
from random import (
    randint,
    choice,
)  # Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import color
from time import sleep

cls = lambda: os.system("clear")  # Clear Console


class NumberGuesser:
    def runGame(self):
        cls()
        userChoice = 1

        while userChoice != 0:
            userChoice = input(
                color.Color.BLUE
                + "Play guess the number!\n1. Play\n0. Exit "
                + color.Color.END
            )
            try:
                userChoice = int(userChoice)
                isInt = True
            except ValueError:
                isInt = False
                print(
                    color.Color.RED
                    + "Invalid input, try a number instead."
                    + color.Color.END
                )
                print(
                    color.Color.RED
                    + "HINT: The only accepted inputs are 1 and 0!"
                    + color.Color.END
                )
                sleep(1.5)

            cls()
            if userChoice == 1:
                self.guessTime()

    def guessTime(self):
        MAX_NUM = 100
        MIN_NUM = 1
        secretNum = randint(MIN_NUM, MAX_NUM)
        userChoice = 0

        while userChoice != secretNum:
            print(
                color.Color.BLUE
                + "I am thinking of a number between "
                + str(MIN_NUM)
                + " and "
                + str(MAX_NUM)
                + "..."
                + color.Color.END
            )
            userChoice = input(
                color.Color.BLUE + "Guess the number: " + color.Color.END
            )
            try:
                userChoice = int(userChoice)
                isInt = True
            except ValueError:
                isInt = False
            if isInt == False:
                print(
                    color.Color.RED
                    + "Invalid input, try a number instead."
                    + color.Color.END
                )
            elif int(userChoice) == secretNum:
                print(color.Color.DARKCYAN + "Wow, that's right!" + color.Color.END)
                sleep(0.5)
                return
            elif int(userChoice) < secretNum:
                print(color.Color.RED + "Higher!" + color.Color.END)
            elif int(userChoice) > secretNum:
                print(color.Color.RED + "Lower!" + color.Color.END)
            else:
                print(color.Color.RED + "Try again!" + color.Color.END)

            sleep(1)
            cls()
