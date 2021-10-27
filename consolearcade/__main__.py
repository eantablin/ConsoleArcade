import sys
import os
## import console, sound 
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
from games import eightball, numberguesser, rockpaperscissors, rpgame, hangman, tictactoe
# from games.rpgFiles import player, enemy, merchant, item
from dependencies import color
from time import sleep


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
		print("NULL Arcade\n\nPick a game\n1. RPG -- In Progress\n2. EightBall -- Stable\n3. NumberGuesser -- Stable\n4. RockPaperScissors -- Stable\n5. HangMan -- Stable\n6. TicTacToe -- In Progress\n7. Load Save -- TBD\n0. Exit")
		gameChoice = int(input('\nChoice: '))
		
		if gameChoice == 1: # Run RPG
			game = rpgame.RPGame()
			game.startGame()
			del game

		elif gameChoice == 2: # Run EightBall
			game = eightball.EightBall()
			game.runGame()
			del game
		
		elif gameChoice == 3: # Run NumberGuesser 
			game = numberguesser.NumberGuesser()	
			game.runGame()
			del game
		
		elif gameChoice == 4: # Run RockPaperScissors
			game = rockpaperscissors.RockPaperScissors()
			game.runGame()
			del game

		elif gameChoice == 5: # Run HangMan
			game = hangman.HangMan()
			game.runGame()
			del game

		elif gameChoice == 6: # Run TicTacToe
			game = tictactoe.TicTacToe()
			game.runGame()
			del game
		
		elif gameChoice == 7: # Load/Create a save file
			print("TBD")
			sleep(1)
			# fileName = input("saveName: ")
			# gameSave = open(fileName, "w+")

		elif gameChoice == 0:
			isAlive = False

main() # Run program