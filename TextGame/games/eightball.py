import os
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors

cls = lambda: os.system('clear') # Clear Console

class EightBall():
	
	def runGame(self):
		cls()
		userChoice = 1
		# sound.play_effect('casino:DieThrow3')
		
		# While user doesnt wanna leave
		while userChoice != 0:

			userChoice = int(input("Be illuminated by the EightBall\n1. Roll ball\n0. Exit"))

			cls()
			
			if userChoice == 1:
				# sound.play_effect('casino:DieShuffle3')
				self.rollBall()
			
	def rollBall(self):
		side = randint(0,7)

		if side == 0:
			print("Believe so\n")
		elif side == 1:
			print("Muddy waters\n")
		elif side == 2:
			print("It's dark\nin here\n")
		elif side == 3:
			print("Yes\n")
		elif side == 4:
			print("Don't bet\non it\n")
		elif side == 5:
			print("Could you\nrepeat that?\n")
		elif side == 6:
			print("No\n")
		elif side == 7:
			print("Sleep on it\n")