import os
from random import randint, choice # Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import color
from time import sleep
from games.rpgFiles import player, enemy, merchant, item

cls = lambda: os.system('clear') # Clear Console

class RPGame():
	
	isAlive = True # Game still running?
	player = player.Player() # Initialize player


	def startGame(self):
		
		# Game setup
		cls()
		# sound.play_effect('game:Click_1')
		
		self.characterChoice(self.player)
		
		while self.isAlive == True and self.player.currentHP > 0:

			# Adventure time
			self.adventure(self.player)
			# TODO implement timer, 1-2 seconds

			if self.player.currentHP <= 0:
				counter = 0
				while counter < 10: # Death screen lasts 5 seconds
					cls()
					print(color.Color.RED + "YOU DIED")
					sleep(0.2)
					cls()
					print(color.Color.BOLD + "YOU DIED" + color.Color.END)
					sleep(0.3)
					counter += 1
					del self.player # Delete player object

				break

		
		return
	
	# Allows user to pick a class
	def characterChoice(self, player):
		
		while self.isAlive == True: # While user hasn't decided to exit
			cls()
			userChoice = int(input(color.Color.DARKCYAN + "Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit\n\nChoice: " + color.Color.END))
			
			if userChoice == 1: # User might pick to be a peasant
				cls()
				## peasantSound()

				print(color.Color.RED + "Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Peasant\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					self.player.classChoice(userChoice)
					return

			elif userChoice == 2: # User might choose a nobleman
				cls()
				## nobleSound()

				print(color.Color.BLUE + "Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					self.player.classChoice(userChoice)
					return
			
			elif userChoice == 3: # Perhaps user went for royalty
				cls()
				## royalSound()

				print(color.Color.BLUE + "Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					self.player.classChoice(userChoice)
					return
					 	
			elif userChoice == 0:
				self.isAlive = False
				return
				
							
	def adventure(self, player):
		
		cls()
		
		while self.isAlive == True:
			cls()
			self.displayStats(self.player)
			userChoice = int(input(color.Color.DARKCYAN + '1. Explore\n2. Inventory\n3. Stats\n0. Exit\n\nChoice: ' + color.Color.END))

			
			if userChoice == 1: # Explore
				
				while userChoice != 0 or self.player.isAlive == True:
					encounter = randint(1, 7)
					if encounter == 1: # Encounter stranger
						cls()
						print("Stranger says hi")
						# TODO: Make stranger interaction
						# Can be a fight, someone with a gift
						# Or they can have important information
						# Allowing one of the players stats to improve
						sleep(1)
						return

					elif encounter == 2: # Traveling merchant
						cls()
						print("A merchant has set up shop across the road")
						merchant = merchant.Merchant() # Initialize merchant
						# TODO: Make merchant interaction
						# Being a child of player class, merchant should onCreate
						# be provided with a selection of 5-10 items
						# which reset every time player sees them
						print("Ah, hello my friend. Care to buy something? I have many fine wares for you today.")
						sleep(1)
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
						print("I found a chest!")
						sleep(1.5)
						it = Item()
						it.createBuff()
						self.player.addinventory(it)
						cls()
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
						self.combat(self.player)
						return

				# In order of priority
				# Add chance for combat, traveling merchant, find treasure, dungeon, town


			elif userChoice == 2: # Inventory
				# player.displayInventory()
				self.player.useItem()
				
			elif userChoice == 3: # self.player stats
				self.playerHP = self.player.getCurrentHP()
				self.playerTotalHP = self.player.getMaxHP()
				if self.playerHP >= self.playerTotalHP * .75: # Top 75% of hp
					print(color.Color.DARKCYAN + "I'll be fine" + color.Color.END)
					sleep(1)
				elif self.playerHP >= self.playerTotalHP * .50 and self.playerHP < self.playerTotalHP * .75: # Between 50 - 75%
					print(color.Color.DARKCYAN + "Some cuts and bruises, I'm otherwise okay" + color.Color.END)
					sleep(1)
				elif self.playerHP >= self.playerTotalHP * .25 and self.playerHP < self.playerTotalHP * .50: # Between 25 - 50%
					print(color.Color.DARKCYAN + "I'll need healing soon" + color.Color.END)
					sleep(1)
				elif self.playerHP >= self.playerTotalHP * .1 and self.playerHP < self.playerTotalHP * .25: # Between 1-25%
					print(color.Color.DARKCYAN + "Need healing, I might not make it" + color.Color.END)
					sleep(1)
				else:
					print(color.Color.DARKCYAN + "I could use some healing" + color.Color.END)
					sleep(1)
			elif userChoice == 0: # Exit game
				self.isAlive = False

	def combat(self, player):

		combatMP = self.player.getMana() # Track mana
		combatEnergy = self.player.getStam() # Track stamina
		randNumber = randint(1, 100) # Create random variable to assign enemy encounter
		willFlee = randint(1,100) # Predetermined chance to flee
		opponent = enemy.Enemy() # Instantiate enemy object
		opponent.randomEnemy(randNumber) # Assign random enemy

		while self.player.currentHP > 0 and opponent.currentHP > 0: # While player and opponent are still in the game

			combatEnergy += 5 # player regenerates stamina

			cls()
			self.displayCombatStats(self.player, combatMP, combatEnergy)
			self.displayEnemyStats(opponent)

			userChoice = input(color.Color.RED + f"{opponent.className}: {opponent.catchPhrase}\n\n1. Slap it over the head\n2. Attempt a takedown\n3. Inventory\n4. Flee\n0. Exit\n\nChoice: " + color.Color.END)
			userChoice = int(userChoice)

			if userChoice == 1: # Standard attack
				combatEnergy -= 10
				opponent.currentHP -= self.player.getDMG()

				if opponent.isAlive() == True:
					self.player.currentHP -= opponent.getDMG()

			elif userChoice == 2: # Strong attack
				combatEnergy -= 20
				opponent.currentHP -= self.player.getDMG() * 2
				
				if opponent.isAlive() == True:
					self.player.currentHP -= opponent.getDMG()
			
			elif userChoice == 3: # Display satchel contents
				# player.displayInventory()
				self.player.useItem()

			elif userChoice == 4: # Attempt to flee
				willFlee = randint(1,100)

				if willFlee > 50:
					print("Phew, that was close")

					sleep(2)
					break
				
				else: # On fail, opponent gets free hit; just git gud
					self.player.currentHP -= opponent.getDMG()
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

		if self.player.isAlive() == True and opponent.isAlive() == False:
			# TODO: Help me work
			# i = Item()
			# i.createBuff()
			# player.addinventory(i)
			print("There's something on the ground\n")
			sleep(1.5)
			it = item.Item()
			it.createBuff()
			self.player.addinventory(it)
			print(f"A {it.name}, nice")
			self.player.checklevelUP(opponent.getXP())
			sleep(2)




	# Rewrite me after Enemy class remake
	def displayEnemyStats(self, Enemy): # Show enemy stats
		print(color.Color.DARKCYAN + f'{Enemy.className} - HP: {Enemy.getCurrentHP()}/{Enemy.getMaxHP()}')

	def displayCombatStats(self, player, mana, stamina): # Keep track of current combat stats
		print(color.Color.DARKCYAN + f'{self.player.className} - HP: {self.player.getCurrentHP()}/{self.player.getMaxHP()} | MP: {mana}/{self.player.getMana()} | EN: {stamina}/{self.player.getStam()}\n' + color.Color.END)
	
	def displayStats(self, player): # For most menus
		print(color.Color.DARKCYAN + f'{self.player.className}\nHP: {self.player.getCurrentHP()}/{self.player.getMaxHP()} | MP: {self.player.getMana()} | XP: {self.player.getXP()}\n ' + color.Color.END)
	
	def displayFullStats(self, player): # For when user wants/needs to see their total stats
		print(color.Color.DARKCYAN + f'{self.player.className}\nHP: {self.player.getCurrentHP()}/{self.player.getMaxHP()} | MP: {self.player.getMana()}\nGP: {self.player.getGP()} | XP: {self.player.getXP()}\n' + color.Color.END)