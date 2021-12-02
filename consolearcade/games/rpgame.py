import os
from random import randint, choice # Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import color
from time import sleep
from games.rpgFiles.player import Player
from games.rpgFiles.enemy import Enemy
from games.rpgFiles.merchant import Merchant
from games.rpgFiles.item import Item

cls = lambda: os.system('clear') # Clear Console

class RPGame():
	
	isAlive = True # Game still running?



	def startGame(self):
		
		# Game setup
		cls()
		# sound.play_effect('game:Click_1')
		player = Player() # Initialize player
		self.characterChoice(player) # Allow player to choose base character
		
		while self.isAlive and player.isAlive: # While game is still running and player isn't dead

			# Adventure time
			self.adventure(player)

			if player.currentHP <= 0: # On player death
				counter = 0
				while counter < 10: # Death screen lasts 5 seconds
					cls()
					print(color.Color.RED + "YOU DIED")
					sleep(0.2)
					cls()
					print(color.Color.BOLD + "YOU DIED" + color.Color.END)
					sleep(0.3)
					counter += 1

		return
	

	def characterChoice(self, player): # Allows user to pick a class
		
		while self.isAlive: # While user hasn't decided to exit
			cls()
			userChoice = int(input(color.Color.DARKCYAN + "Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit\n\nChoice: " + color.Color.END))
			
			if userChoice == 1: # User might pick to be a peasant
				cls()
				## peasantSound()

				print(color.Color.RED + "Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Peasant\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
			elif userChoice == 2: # User might choose a nobleman
				cls()
				## nobleSound()

				print(color.Color.BLUE + "Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others\n\nChoice: " + color.Color.END))
			
			elif userChoice == 3: # Perhaps user went for royalty
				cls()
				## royalSound()

				print(color.Color.PURPLE + "Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others\n\nChoice: " + color.Color.END))
					 	
			elif userChoice == 0: # User chooses to exit
				self.isAlive = False
				return

			if classChoice == 1: # User has picked a class
				player.classChoice(userChoice)
				return
				
							
	def adventure(self, player): # Main game function
		# TODO: Add save/load
	
		while self.isAlive:
			cls()
			self.displayStats(player) # Display current user stats
			userChoice = int(input(color.Color.DARKCYAN + '1. Explore\n2. Inventory\n3. Stats\n0. Exit\n\nChoice: ' + color.Color.END)) 

			
			if userChoice == 1: # Explore
				
				while userChoice != 0 or player.isAlive: # While user hasn't chosen to exit or they're still alive
					encounter = randint(1, 7)
					if encounter == 1: # Encounter stranger
						cls()
						print("Stranger says hi")
						# TODO: Make stranger interaction
						# Can be a fight, someone with a gift
						# Or they can have important information
						# Allowing one of the players stats to improve
						sleep(1.5)
						return

					elif encounter == 2: # Traveling merchant
						cls()
						print("A merchant has set up shop across the road")
						merchant = Merchant() # Initialize merchant
						# TODO: Make merchant interaction
						# Being a child of player class, merchant should onCreate
						# be provided with a selection of 5-10 items
						# which reset every time player sees them
						print("Ah, hello my friend. Care to buy something? I have many fine wares for you today.")
						sleep(1.5)
						del merchant # Goodbye merchant, we encounter different/new ones on the road
						return 
						
					elif encounter == 3: # Find treasure
						cls()
						# TODO: add item variety
						# Maybe there's more than 1 item in there
						# OR maybe the chest is rigged: a trap!
						print("There's a mound in the distance\n")
						sleep(2)
						print(color.Color().BROWN + color.Color().FAINT + "*panting*\n" + color.Color().END)
						sleep(1.2)
						print("I found a chest!")
						sleep(1.5)
						it = Item()
						it.createBuff()
						player.addinventory(it)
						print(f"Nice, a {it.name}. Should come in handy")
						sleep(1.8)
						return 
						
					elif encounter == 4: # Dungeon time
						cls()
						# TODO: Make a dungeon system
						# Higher likelihood of treasure
						# Higher likelihood of combat
						# -- Lower odds of fleeing
						# Lower likelihood of merchant
						# Lower likelihood of stranger
						# -- Higher odds of being negative to player
						
						print("That cave looks interesting, maybe I should go in")
						sleep(1)
						return 
						
					elif encounter == 5: # Found a Town
						cls()
						# TODO: Extra encounters can be found in town
						# If alleyway: oddsOfCombat++
						# else: oddsOfCombat == 5%
						# Implement barbershop: Can heal, or give damage buff
						# damage buff until we implement defenses (armor/shields)
						# Market, a bunch of merchants who the player can jump from and come back to
						# Blacksmith, buy or sell equipment
						# Later on: different types of town
						# Monster/Smithing capital/Merchant city/Hospital/Farmers
						print("A town? Didn't think I'd run into one for a while")
						sleep(2)
						return 
						
					elif encounter > 5: # ATM should have 2 rolls in 7, 28.57% chance
						cls()
						print("There's something up ahead")
						sleep(1)
						self.combat(player)
						return

				# In order of priority
				# Add chance for combat, traveling merchant, find treasure, dungeon, town

			elif userChoice == 2: # Inventory
				player.useItem()
				
			elif userChoice == 3: # player stats
				playerHP = player.getCurrentHP()
				playerTotalHP = player.getMaxHP()
				if playerHP >= playerTotalHP * .75: # Top 75% of hp
					print(color.Color.DARKCYAN + "I'll be fine" + color.Color.END)
					sleep(1)
				elif playerHP >= playerTotalHP * .50 and playerHP < playerTotalHP * .75: # Between 50 - 75%
					print(color.Color.DARKCYAN + "Some cuts and bruises, I'm otherwise okay" + color.Color.END)
					sleep(1)
				elif playerHP >= playerTotalHP * .25 and playerHP < playerTotalHP * .50: # Between 25 - 50%
					print(color.Color.DARKCYAN + "I'll need healing soon" + color.Color.END)
					sleep(1)
				elif playerHP >= playerTotalHP * .1 and playerHP < playerTotalHP * .25: # Between 1-25%
					print(color.Color.DARKCYAN + "Need healing, I might not make it" + color.Color.END)
					sleep(1)
				else:
					print(color.Color.DARKCYAN + "I could use some healing" + color.Color.END)
					sleep(1)

			elif userChoice == 0: # Exit game
				self.isAlive = False

	def combat(self, player):

		combatMP = player.getMana() # Track mana
		combatEnergy = player.getStam() # Track stamina
		randNumber = randint(1, 100) # Create random variable to assign enemy encounter
		willFlee = 0 # Predetermined chance to flee
		opponent = Enemy() # Instantiate enemy object
		opponent.randomEnemy(randNumber) # Assign random enemy

		while player.currentHP > 0 and opponent.currentHP > 0: # While player and opponent are still in the game

			combatEnergy += 5 # player regenerates stamina

			cls()
			self.displayCombatStats(player, combatMP, combatEnergy)
			self.displayEnemyStats(opponent)

			userChoice = input(color.Color.RED + f"{opponent.className}: {opponent.catchPhrase}\n\n1. Slap it over the head\n2. Wack it with a stick\n3. Inventory\n4. Flee\n0. Exit\n\nChoice: " + color.Color.END)
			userChoice = int(userChoice)

			if userChoice == 1: # Standard attack
				combatEnergy -= 10
				opponent.currentHP -= player.getDMG()

				if opponent.isAlive() == True:
					player.currentHP -= opponent.getDMG()

			elif userChoice == 2: # Strong attack
				combatEnergy -= 20
				opponent.currentHP -= player.getDMG() * 2
				
				if opponent.isAlive() == True:
					player.currentHP -= opponent.getDMG()
			
			elif userChoice == 3: # Display satchel contents
				player.useItem()

			elif userChoice == 4: # Attempt to flee
				willFlee = randint(1,100)

				if willFlee > 50:
					print("Phew, that was close")

					sleep(2)
					break
				
				else: # On fail, opponent gets free hit; just git gud
					player.currentHP -= opponent.getDMG()
					print(f"{opponent.className}: No escape!")
					sleep(1)
			
			elif userChoice == 0:
				self.isAlive = False
				break

			## TODO
			# Win/loss conditions
			# elif player.currentHP <= 0:
			# 	break
			# elif opponent.currentHP <= 0:
			# 	player.inventory.append(opponent.)

		if player.isAlive() == True and opponent.isAlive() == False: # Player survived: rewards
			# TODO: Help me work
			print("There's something on the ground\n")
			sleep(1.5)
			it = Item()
			it.createBuff()
			player.addinventory(it)
			print(f"A {it.name}, nice")
			player.checklevelUP(opponent.getXP())
			sleep(2)

	# Rewrite me after Enemy class remake
	def displayEnemyStats(self, Enemy): # Show enemy stats
		print(color.Color.DARKCYAN + f'{Enemy.className} - HP: {Enemy.getCurrentHP()}/{Enemy.getMaxHP()}')

	def displayCombatStats(self, player, mana, stamina): # Keep track of current combat stats
		print(color.Color.DARKCYAN + f'{player.className} - HP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {mana}/{player.getMana()} | EN: {stamina}/{player.getStam()}\n' + color.Color.END)
	
	def displayStats(self, player): # For most menus
		print(color.Color.DARKCYAN + f'{player.className} - HP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {player.getMana()} | XP: {player.getXP()}\n ' + color.Color.END)
	
	def displayFullStats(self, player): # For when user wants/needs to see their total stats
		print(color.Color.DARKCYAN + f'{player.className} - HP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {player.getMana()}\nGP: {player.getGP()} | XP: {player.getXP()}\n' + color.Color.END)