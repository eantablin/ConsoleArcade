import os
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import eightballascii

cls = lambda: os.system('clear') # Clear Console

class EightBall():
	
	def runGame(self):
		cls()
		userChoice = 1
		# sound.play_effect('casino:DieThrow3')
		
		# While user doesnt wanna leave
		while userChoice != 0:

			userChoice = int(input("Be illuminated by the EightBall\n1. Roll ball\n0. Exit "))

			cls()
			
			if userChoice == 1:
				# sound.play_effect('casino:DieShuffle3')
				self.rollBall()
			
	def rollBall(self):
		side = randint(0,7)

		if side == 0:
			print(eightballascii.eightBall0)
		elif side == 1:
			print(eightballascii.eightBall1)
		elif side == 2:
			print(eightballascii.eightBall2)
		elif side == 3:
			print(eightballascii.eightBall3)
		elif side == 4:
			print(eightballascii.eightBall4)
		elif side == 5:
			print(eightballascii.eightBall5)
		elif side == 6:
			print(eightballascii.eightBall6)
		elif side == 7:
			print(eightballascii.eightBall7)