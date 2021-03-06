import os
import time
from random import (
    randint,
    choice,
)  # Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import color

cls = lambda: os.system("clear")  # Clear Console


class RockPaperScissors:

    # t = 10000000 # For Ghetto Timer

    def runGame(self):
        cls()
        userChoice = 1
        while userChoice != 0:  # While the user does not want to quit to game menu
            userChoice = input(
                color.Color.BLUE
                + "Play Rock Paper Scissors!\n1. Play\n0. Exit "
                + color.Color.END
            )

            try:
                userChoice = int(userChoice)
                isInt = True
            except ValueError:
                print(
                    color.Color.RED
                    + "Invalid selection, try a number instead!"
                    + color.Color.END
                )
                print(
                    color.Color.RED
                    + "The only valid selections are 1 and 0!"
                    + color.Color.END
                )
                time.sleep(1.5)

            cls()
            if userChoice == 1:  # Start the game
                self.rockPaperScissors()

    # def ghettoTimer(self):
    # 	time = [] # For Ghetto Timer
    # 	for i in range(0, self.t): # Ghetto Timer
    # 		time.append(i)
    # 	cls()

    def rockPaperScissors(self):
        playOptions = ["rock", "paper", "scissors"]
        userWin = False
        while userWin != True:
            userChoice = str(
                input(
                    color.Color.BLUE
                    + "What is your choice? (rock/paper/scissors)\n0. Exit "
                    + color.Color.END
                )
            )
            userChoice.lower()  # converts userChoice to all lowercase
            compChoice = choice(
                playOptions
            )  # Selects a 'random' play choice for the computer
            if (
                userChoice == "rock" or userChoice == "r"
            ):  # Options for if the user selects Rock
                print(color.Color.BLUE + "You chose rock..." + color.Color.END)
                userChoice = "rock"
                print(
                    color.Color.BLUE
                    + "Computer chose "
                    + compChoice
                    + "..."
                    + color.Color.END
                )
                if userChoice == compChoice:  # If userChoice is the same as compChoice
                    print(color.Color.RED + "It's a draw!" + color.Color.END)
                    time.sleep(1)
                elif compChoice == "paper":  # If user loses
                    print(color.Color.RED + "You lose!" + color.Color.END)
                    time.sleep(1)
                else:  # If user wins
                    print(color.Color.RED + "You win!" + color.Color.END)
                    time.sleep(1)
                    userWin = True
            elif (
                userChoice == "paper" or userChoice == "p"
            ):  # Options for if the user selects Paper
                print(color.Color.BLUE + "You chose paper..." + color.Color.END)
                userChoice = "paper"
                print(
                    color.Color.BLUE
                    + "Computer chose "
                    + compChoice
                    + "..."
                    + color.Color.END
                )
                if userChoice == compChoice:  # If userChoice is the same as compChoice
                    print(color.Color.RED + "It's a draw!" + color.Color.END)
                    time.sleep(1)
                elif compChoice == "scissors":  # If user loses
                    print(color.Color.RED + "You lose!" + color.Color.END)
                    time.sleep(1)
                else:  # If user wins
                    print(color.Color.RED + "You win!" + color.Color.END)
                    time.sleep(1)
                    userWin = True
            elif (
                userChoice == "scissors" or userChoice == "s"
            ):  # Options for if the user selects Scissors
                print(color.Color.BLUE + "You chose scissors..." + color.Color.END)
                userChoice = "scissors"
                print(
                    color.Color.BLUE
                    + "Computer chose "
                    + compChoice
                    + "..."
                    + color.Color.END
                )
                if userChoice == compChoice:  # If userChoice is the same as compChoice
                    print("It's a draw!")
                    time.sleep(1)
                elif compChoice == "rock":  # If user loses
                    print(color.Color.RED + "You lose!" + color.Color.RED)
                    time.sleep(1)
                else:  # If user wins
                    print(color.Color.RED + "You win!" + color.Color.END)
                    time.sleep(1)
                    userWin = True
            elif userChoice == "0":  # If user wants to quit
                return 0
            else:  # If user puts an invalid choice
                print(
                    color.Color.BLUE + "That is not a valid choice." + color.Color.END
                )
                time.sleep(1)
