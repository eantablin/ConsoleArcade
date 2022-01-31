import sys
import os
## import console, sound 
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
from games import eightball, numberguesser, rockpaperscissors, rpgame, hangman, tictactoe, blackjack
from dependencies import color
from time import sleep


# Shorthand functions 
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
		print("NULL Arcade\n\nPick a game\n1. RPG -- In Progress\n2. EightBall -- Stable\n3. NumberGuesser -- Stable\n4. RockPaperScissors -- Stable\n5. HangMan -- Stable\n6. TicTacToe -- In Progress\n7. Blackjack -- In Progress\n8. Load Save -- TBD\n0. Exit")
		gameChoice = input('\nChoice: ')

		try: # Try to make user input an int, is used in most of the games
			gameChoice = int(gameChoice) # Try to make gameChoice an int value
			isInt = True
		except ValueError: # If gameChoice is a str value
			isInt = False
			print(color.Color.RED + "Invalid input, try a number instead." + color.Color.END)
			sleep(1.5)
		
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
		
		elif gameChoice == 7: # Run Blackjack
			game = blackjack.Blackjack()
			game.runGame()
			del game

		elif gameChoice == 8: # Load/Create a save file
			print("TBD")
			sleep(1)
			# fileName = input("saveName: ")
			# gameSave = open(fileName, "w+")

		elif gameChoice == 0:
			isAlive = False
		
		else:
			print(color.Color.RED + "Invalid selection, try again." + color.Color.END)
			sleep(1)

main() # Run program