import sys
import os
## import console, sound 
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
import eightball
import numberguesser
import rockpaperscissors
import rpgame
import hangman


# Shorthand functions 
## cls = lambda: console.clear() # Clear console
cls = lambda: os.system('clear') # Clear Console
## peasantSound = lambda: sound.play_effect('8ve:8ve-beep-timber') # Peasant's signature sound
## nobleSound = lambda: sound.play_effect('game:Woosh_1') # Nobleman's signature sound
## royalSound = lambda: sound.play_effect('game:Ding_3') # Royalty's signature sound
easyaddition = lambda: print("Hello World")


def main():
	
	isAlive = True
	
	while isAlive == True:
	
		cls()
		# sound.play_effect('digital:HighDown')
		print("NULL Arcade\n\nPick a game\n1. RPG -- In Progress\n2. EightBall -- Stable\n3. Load Save -- TBD\n4. NumberGuesser -- Stable\n5. RockPaperScissors -- Stable\n6. HangMan -- In Progress\n0. Exit")
		gameChoice = int(input())
		
		if gameChoice == 1: # Run RPG
			game = rpgame.RPGame()
			player = rpgame.Player()
			game.startGame(player)
			del game, player


		elif gameChoice == 2: # Run EightBall
			game = eightball.EightBall()
			# game = EightBall()
			game.runGame()
			del game
		
		elif gameChoice == 3: # Load/Create a save file 
			print("TBD")
			# fileName = input("saveName: ")
			# gameSave = open(fileName, "w+")
		
		elif gameChoice == 4: # Run NumberGuesser
			game = numberguesser.NumberGuesser()
			game.runGame()
			del game

		elif gameChoice == 5: # Run RockPaperScissors
			game = rockpaperscissors.RockPaperScissors()
			game.runGame()
			del game

		elif gameChoice == 6:
			game = hangman.HangMan()
			game.runGame()
			del game

		elif gameChoice == 0:
			isAlive = False

main() # Run program
