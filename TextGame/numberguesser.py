import os
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
import color

cls = lambda: os.system('clear') # Clear Console

class NumberGuesser():

	def runGame(self):
		cls()
		userChoice = 1
		while userChoice != 0:
			userChoice = int(input(color.Color.BLUE + "Play guess the number!\n1. Play\n0. Exit" + color.Color.END))
			cls()
			if userChoice == 1:
				self.guessTime()
	
	def guessTime(self):
		MAX_NUM = 100
		MIN_NUM = 1
		secretNum = randint(MIN_NUM, MAX_NUM)
		userChoice = 0

		while userChoice != secretNum:
			print(color.Color.BLUE + "I am thinking of a number between " + str(MIN_NUM) + " and " + str(MAX_NUM) + "..." + color.Color.END)
			userChoice = int(input(color.Color.BLUE + "Guess the number: " + color.Color.END))
			if userChoice == secretNum:
				print(color.Color.DARKCYAN + "Wow, that's right!" + color.Color.END)
			elif userChoice < secretNum:
				print(color.Color.RED + "Higher!" + color.Color.END)
			elif userChoice > secretNum:
				print(color.Color.RED + "Lower!" + color.Color.END)
			else:
				print(color.Color.RED + "Try again!" + color.Color.END)