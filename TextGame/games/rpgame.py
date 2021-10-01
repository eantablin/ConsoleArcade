import os
from random import randint, choice# Used for eightBall, numberGuesser, rockPaperScissors
from dependencies import color
from time import sleep

cls = lambda: os.system('clear') # Clear Console

class Player():
	level = 0 # Track progress
	health = 0 # Track HP
	currentHP = health
	stamina = 0 # Track energy
	mana = 0 # Track magic potential
	xp = 0 # Track level-up progress
	gp = 0 # Track gold pieces (currency)
	className = '' # Track classtype
	DMG = 0
	inventory = []
	catchPhrase = ""


	
	# Classes will be set default values according to characteristics
	def classChoice(self, choice): # Initial class choice

		if choice == 1: # Peasant
			## peasantSound()
			self.level = 1
			self.health = 60
			self.currentHP = self.health
			self.stamina = 80
			self.mana = 0 
			self.xp = 0
			self.gp = 0
			self.className = "Peasant"
			self.DMG = 10
			# Total = 140
		elif choice == 2: # Nobleman
			## nobleSound()
			self.level = 1
			self.health = 100
			self.currentHP = self.health
			self.stamina = 50
			self.mana = 5
			self.xp = 0
			self.gp = 80
			self.className = "Nobleman"
			self.dmg = 12
			# Total = 155
		elif choice == 3: # Royalty
			## royalSound()
			self.level = 1
			self.health = 100
			self.currentHP = self.health
			self.stamina = 30
			self.mana = 15
			self.xp = 0
			self.gp = 200
			self.className = "Royalty"
			self.dmg = 15
			# Total = 145
		
		cls()
		
	# Use on user XP gain
	# Perhaps later make it so bosses can level up too
	def checklevelUP(self, experience):

		totalXP = self.getXP() + experience # Keep track of current total experience

		while totalXP >= 100:

			if self.className == "Peasant": 
				self.setHP(self.getHP() + 10)
				self.setStam(self.getStam() + 6)
				self.setMana(self.getMana() + 5)
				self.setDMG(self.getDMG() + 5)
				# Total = 26
				
			elif self.className == "Nobleman":
				self.setHP(self.getHP() + 4)
				self.setStam(self.getStam() + 4)
				self.setMana(self.getMana() + 8)
				self.setDMG(self.getDMG() + 3)
				# Total = 19
			
			elif self.className == "Royalty":
				self.setHP(self.getHP() + 2)
				self.setStam(self.getStam() + 3)
				self.setMana(self.getMana() + 10)
				self.setDMG(self.getDMG() + 1)
				# Total = 16

			# sound.play_effect('arcade:Powerup_1')
			self.level += 1 # Base upgrade
			self.currentHP = self.health # Reset HP to max // Free heal
			totalXP -= 100
		
		if totalXP < 100: # Keep track of total XP
			self.setXP(totalXP)
		
	def isAlive(self):
		if self.currentHP > 0:
			return True
		else:
			return False
			
	# Getters and setters
	#
	# Level Functionality
	def getLVL(self):
		return self.level
	def setLVL(self, value):
		self.level = value
	def changeLVL(self, value):
		self.level += value
	
	# Experience Functionality
	def getXP(self):
		return self.xp
	def setXP(self, value):
		self.xp = value
	def changeXP(self, value):
		self.xp += value
		
	# Total HP Functionality
	def getHP(self):
		return self.health
	def setHP(self, value):
		self.health = value
	def changeHP(self, value):
		self.health += value

	# Current HP Functionality
	def getCurrentHP(self):
		return self.currentHP
	def setCurrentHP(self, value):
		self.currentHP = value
	def changeCurrentHP(self, value):
		self.currentHP += value
	
	# Stamina Functionality
	def getStam(self):
		return self.stamina
	def setStam(self, value):
		self.stamina = value
	def changeStam(self, value):
		self.stamina += value
	
	# Mana Functionality
	def getMana(self):
		return self.mana
	def setMana(self, value):
		self.mana = value
	def changeMana(self, value):
		self.mana += value
		
	# Gold piece Functionality
	def getGP(self):
		return self.gp
	def setGP(self, value):
		self.gp = value
	def changeGP(self, value):
		self.gp += value

	# Damage Functionality
	def getDMG(self):
		return self.DMG
	def setDMG(self, value):
		self.DMG = value
	def changeDMG(self, value):
		self.DMG += value

	# CatchPhrase Functionality
	def getcatchPhrase(self):
		return self.catchPhrase
	def setcatchPhrase(self, value):
		self.catchPhrase = value

	# Inventory Functionality
	def getinventory(self):
		return self.inventory
	def setinventory(self, value): # Instantly arrange inventory
		self.inventory = value
	def addinventory(self, value):
		self.inventory.append(value)
	def removeinventory(self, itemToRemove): # self, value to remove
		# TODO: OPTIMIZE ME!
		counter = 0
		for i in self.inventory:
			if i == itemToRemove:
				self.inventory.pop(i)
				return
			counter += 1
	
class Enemy(Player):

	# def __init__(self, _HP, _MP, _XP, _DMG):
	# 	self.HP = _HP
	# 	self.MP = _MP
	# 	self.XP = _XP
	# 	self.DMG = _DMG

	def randomEnemy(self, number): # Takes a number between 1-100, set enemy depending on user luck

		if number <= 10: # Strong mob, 10% chance
			self.health = 80
			self.mana = 10
			self.xp = 50
			self.DMG = 20
			self.gp = 50
			self.className = "Troll"
			self.catchPhrase = "MMm yum yum hoo min"
		elif number <= 50 and number > 10: # Trash mob, 40% chance
			self.health = 20
			self.mana = 0
			self.xp = 10
			self.DMG = 5
			self.gp = 10
			self.className = "Goblin"
			self.catchPhrase = "Givs us the gold, givs us!"
		elif number <= 80 and number > 50: # Tier 2 trash mob, 30% chance
			self.health = 30
			self.mana = 0
			self.xp = 20
			self.DMG = 10
			self.gp = 20
			self.className = "Orc"
			self.catchPhrase = "Orcun like human, Orcun eat human."
		elif number <= 85 and number > 80: # Free xp mob, 5% chance
			self.health = 40
			self.mana = 0
			self.xp = 30
			self.DMG = 0
			self.gp = 20
			self.className = "Bear cub"
			self.catchPhrase = "bearcubscreeches.mp3"
		elif number <= 90 and number > 85: # Boss mob, 5% chance
			self.health = 80
			self.mana = 40
			self.xp = 60
			self.DMG = 30
			self.gp = 100
			self.className = "Wizard"
			self.catchPhrase = "Away, fiend!"
		elif number <= 100 and number > 90: # Medium mob, 10% chance
			self.health = 100
			self.mana = 0
			self.xp = 40
			self.DMG = 15
			self.gp = 40
			self.className = "Ogre"
			self.catchPhrase = "Gib shiny!"
		
		self.currentHP = self.health # Same for all

## TODO
# Make merchant class, a store that the user can interact with even choose to attack or just attempt to steal (penalty of buffing enemy/free dmg)
class Merchant(Player):
	

	def encounter(self, player: Player): # Unluckily run into player
		cls() # Clean console
		


	def exist(self): # Object comes to initial existance
		ranNum = randint(1, 100)
	
class Item():
	name = "" # Item name
	price = 0 # Item price
	attribute = "" # Item type
	rarity = 0 # Common, Rare, Heroic, Legendary


class Buff(Item):
	health = 0 # Healing
	healthRegen = 0 # Heal Over Time
	damage = 0
	
	mana = 0 # Mana Influx
	managRegen = 0


	def createBuff(self, attribute):
		return


# class Debuff(Item):

# class Junk(Item):

# class Equipment(Item):






class RPGame():
	
	isAlive = True # Game still running?
	
	def startGame(self, player):
		
		# Game setup
		cls()
		# sound.play_effect('game:Click_1')
		self.characterChoice(player)
		
		while self.isAlive == True and player.currentHP > 0:

			# Adventure time
			self.adventure(player)
			# TODO implement timer, 1-2 seconds
		
		return
	
	# Allows user to pick a class
	def characterChoice(self, player):
		
		while self.isAlive == True: # While user hasn't decided to exit
			cls()
			userChoice = int(input(color.Color.DARKCYAN + "Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit\n" + color.Color.END))
			
			if userChoice == 1: # User might pick to be a peasant
				cls()
				## peasantSound()

				print(color.Color.RED + "Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Peasant\n0. No, let me check others\n" + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return

			elif userChoice == 2: # User might choose a nobleman
				cls()
				## nobleSound()

				print(color.Color.BLUE + "Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others\n" + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
			
			elif userChoice == 3: # Perhaps user went for royalty
				cls()
				## royalSound()

				print(color.Color.PURPLE + "Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others\n" + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
					 	
			elif userChoice == 0:
				self.isAlive = False
				return
				
							
	def adventure(self, player):
		
		cls()
		
		while self.isAlive == True:
			self.displayStats(player)
			userChoice = int(input(color.Color.DARKCYAN + '1. Explore\n2. Inventory\n3. Stats\n0. Exit\n' + color.Color.END))
			cls()
			
			if userChoice == 1: # Explore
				
				while userChoice != 0 or player.isAlive == True:
					encounter = randint(1, 7)
					if encounter == 1:
						return
						# Encounter stranger
					elif encounter == 2:
						return 
						# Traveling merchant
					elif encounter == 3:
						return 
						# Find treasure
					elif encounter == 4: 
						return 
						# Dungeon time
					elif encounter == 5:
						return 
						# Found a Town
					elif encounter > 5: # ATM should have 2 rolls in 7, 28.57% chance
						self.combat(player)
						return

				# In order of priority
				# Add chance for combat, traveling merchant, find treasure, dungeon, town


			elif userChoice == 2: # Inventory

				# TODO
				# Properly implement displaying inventory
				player.addinventory("apples")
				inventory = player.getinventory()
				inventoryLength = len(inventory)

				if inventoryLength > 0: # If there's something in inventory
					for i in inventory: # Loop through it's entirety
						print(color.Color.DARKCYAN + f"{i}" + color.Color.END) # Output each slot

				else: # Empty satchel
					print("My satchel is empty.")


			elif userChoice == 3: # Player stats
				playerHP = player.getCurrentHP()
				playerTotalHP = player.getHP()
				if playerHP >= playerTotalHP * .75:
					print(color.Color.DARKCYAN + "I'll be fine" + color.Color.END)
				elif playerHP >= playerTotalHP * .50 and playerHP < playerTotalHP * .75:
					print(color.Color.DARKCYAN + "Some cuts and bruises, I'm otherwise okay" + color.Color.END)
				elif playerHP >= playerTotalHP * .25 and playerHP < playerTotalHP * .50:
					print(color.Color.DARKCYAN + "I'll need healing soon" + color.Color.END)
				elif playerHP >= playerTotalHP * .1 and playerHP < playerTotalHP * .25:
					print(color.Color.DARKCYAN + "Need healing, I might not make it" + color.Color.END)
				else:
					print(color.Color.DARKCYAN + "I could use some healing" + color.Color.END)
			elif userChoice == 0: # Exit game
				self.isAlive = False

	def combat(self, player):

		combatMP = player.getMana() # Track mana
		combatEnergy = player.getStam() # Track stamina
		randNumber = randint(1, 100) # Create random variable to assign enemy encounter
		willFlee = randint(1,100) # Predetermined chance to flee
		opponent = Enemy() # Instantiate enemy object
		opponent.randomEnemy(randNumber) # Assign random enemy

		while player.currentHP > 0 and opponent.currentHP > 0: # While player and opponent are still in the game

			combatEnergy += 5 # Player regenerates stamina

			cls()
			self.displayCombatStats(player, combatMP, combatEnergy)
			self.displayCombatStatsEnemy(opponent)

			userChoice = input(color.Color.RED + f"{opponent.className}: {opponent.catchPhrase}\n\n1. Slap it over the head\n2. Attempt a takedown\n3. Inventory\n4. Flee\n0. Exit\n" + color.Color.END)
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
				self.displayInventory(player)

			elif userChoice == 4: # Attempt to flee
				willFlee = randint(1,100)

				if willFlee > 50:
					print("Phew, that was close")

					sleep(2)
					break
				
				else: # On fail, opponent gets free hit; just git gud
					player.currentHP -= opponent.getDMG()

			
			elif userChoice == 0:
				self.isAlive = False
				break

			## TODO
			# Win/loss conditions
			# elif player.currentHP <= 0:
			# 	break
			# elif opponent.currentHP <= 0:
			# 	player.inventory.append(opponent.)

		if player.isAlive() == True:
			player.addinventory("Health Potion")
			player.checklevelUP(opponent.getXP())



	# Rewrite me after Enemy class remake
	def displayCombatStatsEnemy(self, Enemy): # Show enemy stats
		print(color.Color.DARKCYAN + f'{Enemy.className} - HP: {Enemy.getCurrentHP()}/{Enemy.getHP()}')

	def displayCombatStats(self, player, mana, stamina): # Keep track of current combat stats
		print(color.Color.DARKCYAN + f'{player.className} - HP: {player.getCurrentHP()}/{player.getHP()} | MP: {mana}/{player.getMana()} | EN: {stamina}/{player.getStam()}\n' + color.Color.END)
	
	def displayStats(self, player): # For most menus
		print(color.Color.DARKCYAN + f'{player.className}\nHP: {player.getCurrentHP()}/{player.getHP()} | MP: {player.getMana()}\n' + color.Color.END)
	
	def displayFullStats(self, player): # For when user wants/needs to see their total stats
		print(color.Color.DARKCYAN + f'{player.className}\nHP: {player.getCurrentHP()}/{player.getHP()} | MP: {player.getMana()}\nGP: {player.getGP()} | XP: {player.getXP()}\n' + color.Color.END)
		
	
	def displayInventory(self, player):
		inv = player.getinventory()
		for i in inv:
			print(i)
		input()

		# print(f'player.')