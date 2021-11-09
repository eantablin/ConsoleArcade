import os
import time
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import eightballascii, color

cls = lambda: os.system('clear') # Clear Console

class EightBall():
	
	def runGame(self):
		cls()
		userChoice = 1
		# sound.play_effect('casino:DieThrow3')
		
		# While user doesnt wanna leave
		while userChoice != 0:

			userChoice = input(color.Color.DARKCYAN + "Be illuminated by the EightBall\n1. Roll ball\n0. Exit " + color.Color.END)
			try:
				userChoice = int(userChoice)
				isInt = True
			except ValueError:
				isInt = False
				print(color.Color.RED + "Invalid input, try a number instead." + color.Color.END)
				print(color.Color.RED + "HINT: The only accepted inputs are 1 and 0!" + color.Color.END)
				time.sleep(1.5)
			cls()
			if userChoice == 1:
				# sound.play_effect('casino:DieShuffle3')
				self.rollBall()
			
	def rollBall(self):
		side = randint(0,7)

		if side == 0:
			print(color.Color.DARKCYAN + eightballascii.eightBall0 + color.Color.END)
		elif side == 1:
			print(color.Color.DARKCYAN + eightballascii.eightBall1 + color.Color.END)
		elif side == 2:
			print(color.Color.DARKCYAN + eightballascii.eightBall2 + color.Color.END)
		elif side == 3:
			print(color.Color.DARKCYAN + eightballascii.eightBall3 + color.Color.END)
		elif side == 4:
			print(color.Color.DARKCYAN + eightballascii.eightBall4 + color.Color.END)
		elif side == 5:
			print(color.Color.DARKCYAN + eightballascii.eightBall5 + color.Color.END)
		elif side == 6:
			print(color.Color.DARKCYAN + eightballascii.eightBall6 + color.Color.END)
		elif side == 7:
			print(color.Color.DARKCYAN + eightballascii.eightBall7 + color.Color.END)