import os
from random import randint, choice # Used for eightBall, numberGuesser, rockPaperScissors
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
				self.setMaxHP(self.getMaxHP() + 10)
				self.setStam(self.getStam() + 6)
				self.setMana(self.getMana() + 5)
				self.setDMG(self.getDMG() + 5)
				# Total = 26
				
			elif self.className == "Nobleman":
				self.setMaxHP(self.getMaxHP() + 4)
				self.setStam(self.getStam() + 4)
				self.setMana(self.getMana() + 8)
				self.setDMG(self.getDMG() + 3)
				# Total = 19
			
			elif self.className == "Royalty":
				self.setMaxHP(self.getMaxHP() + 2)
				self.setStam(self.getStam() + 3)
				self.setMana(self.getMana() + 10)
				self.setDMG(self.getDMG() + 1)
				# Total = 16

			# sound.play_effect('arcade:Powerup_1')
			self.level += 1 # Base upgrade
			self.currentHP = self.health # Reset HP to max // Free heal
			totalXP -= 100
			print("I feel stronger!")
			sleep(3)
		
		if totalXP < 100: # Keep track of total XP
			self.setXP(totalXP)
		
	# TODO: Currently capable of overhealing
	# Is it a bug? No, it's a feature
	# Make it so user can just pick item 0 or 1, etc..
	# User might not expect to make an exact match for item	
	def useItem(self):

		'''
		1) Apples
		2) Tomatoes
		3) Health Potion

		Choice: 
		'''
		userChoice = ""

		while userChoice != 0:  # While user isn't done scrounging around inventory
			# TODO
			# Properly implement displaying inventory
			cls() # Reset screen
			it = Item()
			it.createBuff()
			
			self.addinventory(it) # Testing if items work
			inventory = self.getinventory()
			inventoryLength = len(inventory)

			counter = 1 # Display items from 1..N, skipping 0 due to exit condition

			if inventoryLength > 0: # If there's something in inventory
				for i in inventory: # Loop through it's entirety
					print(color.Color.DARKCYAN + f"{counter}) {i.name}" + color.Color.END) # Output each slot
					counter += 1 # Increase reference value by 1
			

			else: # Empty satchel, break out of loop
				print("My satchel is empty.")
				sleep(1)
				break
				
			print("0) Exit\n")

			# Item usage below
			userChoice = int(input(color.Color.DARKCYAN + "Which item will you use?\n\nChoice: " + color.Color.END))

			if userChoice != 0:
				currItem = inventory[userChoice-1] # -1 to account for 0 consistently being exit condition
			else: 
				break

			# Confirming Item usage
			cls()
			confirmChoice = int(input(f"Use {currItem.name}?\n\n1) Yes\n0) No\n\nChoice: "))
			# TODO: Change item action dependant on it's strengths; i.e: Healing items will change hp, mana MP, etc..
			if confirmChoice == 1:
				self.changeCurrentHP(currItem.healthRegen) #
				del inventory[userChoice-1]
			else:
				userChoice = ""
				continue
			# print(inventory[userChoice])


			# if userChoice in inventory:
			# 	if userChoice == "Apples":
			# 		print(color.Color.DARKCYAN + "You eat the apples and recover some health" + color.Color.END)
			# 		self.changeCurrentHP(5)
			# 		self.removeinventory("Apples")
			# 		sleep(1)
			# 	elif userChoice == "Health Potion":
			# 		print(color.Color.DARKCYAN + "You use the Health Potion and recover health" + color.Color.END)
			# 		self.changeCurrentHP(20)
			# 		self.removeinventory("Health Potion")
			# 		sleep(1)
			# 	else:
			# 		print(color.Color.RED + "You don't have that item..." + color.Color.END)
			# 		sleep(1)

	def displayInventory(self):

		# TODO
		# Properly implement displaying inventory
		cls()
		self.addinventory("Apples")
		inventory = self.getinventory()
		inventoryLength = len(inventory)
		counter = 1

		if inventoryLength > 0: # If there's something in inventory
			for i in inventory: # Loop through it's entirety
				print(color.Color.DARKCYAN + f"{counter}) {i}" + color.Color.END) # Output each slot
				counter += 1

		else: # Empty satchel
			print("My satchel is empty.")

		# print(f'player.')
	
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
	def getMaxHP(self):
		return self.health
	def setMaxHP(self, value):
		self.health = value
	def changeMaxHP(self, value):
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
				self.inventory.remove(i)
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
	rarity = "" # Common, Rare, Heroic, Legendary
	healthRegen = 0 # Direct healing
	healthOverTime = 0 # Heal over Time, HoT
	manaRegen = 0 # Mana intake
	manaOverTime = 0 # Mana intake over time, to prevent spell spamming, most common
	autoDamage = 0 # Damage taken by using item
	autoDamageOverTime = 0 # Damage taken by using item, over time
	damage = 0 # Damage increase
	damageOverTime = 0 # Attacks apply a DoT
	description = "" # Item lore/characteristics
	canCook = False # Can item be cooked? # TODO: Properly implement me later

	def createBuff(self):
		ranNum = randint(1, 100)
		self.attribute = "buff"

		if ranNum <= 10: # Health Potion, 10% chance
			self.name = "Health Potion"
			self.price = 20
			self.rarity = "Common"
			self.healthRegen = 20
			self.description = "This bottle has some heft to it, and a pungent smell"
			self.canCook = False
		elif ranNum <= 50 and ranNum > 10: # Apples, 40% chance
			self.name = "Apples"
			self.price = 5
			self.rarity = "Common"
			self.healthRegen = 5
			self.description = "Red, crispy apple"
			self.canCook = True
		elif ranNum <= 80 and ranNum > 50: # Soup, 30% chance
			self.name = "Soup"
			self.price = 10
			self.rarity = "Common"
			self.healthRegen = 10
			self.description = "A hearty soup stored in a jar, maybe it'd taste better cooked?"
			self.canCook = True
		elif ranNum <= 85 and ranNum > 80: # Mana potion, 5% chance
			self.name = "Mana Potion"
			self.price = 30
			self.rarity = "Common"
			self.manaRegen = 20
			self.description = "Blue viscous liquid, is it looking at me?"
			self.canCook = False
		elif ranNum <= 90 and ranNum > 85: # Small Health Potion, 5% chance
			self.name = "Small Health Potion"
			self.price = 10
			self.rarity = "Common"
			self.healthRegen = 15
			self.description = "Red tones in a small bottle, better not drop it"
			self.canCook = False
		elif ranNum <= 100 and ranNum > 90: # Small Mana Potion, 10% chance
			self.name = "Small Mana Potion"
			self.price = 15
			self.rarity = "Common"
			self.manaRegen = 10
			self.description = "Blue tones in an oddly shaped triangular bottle"
			self.canCook = False

	def createDebuff(self):
		self.attribute = "debuff"
		return
	def createJunk(self):
		self.attribute = "junk"
		return
	def createEquipment(self):
		self.attribute = "equipment"
		return
	
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
			userChoice = int(input(color.Color.DARKCYAN + "Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit\n\nChoice: " + color.Color.END))
			
			if userChoice == 1: # User might pick to be a peasant
				cls()
				## peasantSound()

				print(color.Color.RED + "Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Peasant\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return

			elif userChoice == 2: # User might choose a nobleman
				cls()
				## nobleSound()

				print(color.Color.BLUE + "Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
			
			elif userChoice == 3: # Perhaps user went for royalty
				cls()
				## royalSound()

				print(color.Color.BLUE + "Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n" + color.Color.END)
				classChoice = int(input(color.Color.DARKCYAN + "Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others\n\nChoice: " + color.Color.END))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
					 	
			elif userChoice == 0:
				self.isAlive = False
				return
				
							
	def adventure(self, player):
		
		cls()
		
		while self.isAlive == True:
			cls()
			self.displayStats(player)
			userChoice = int(input(color.Color.DARKCYAN + '1. Explore\n2. Inventory\n3. Stats\n0. Exit\n\nChoice: ' + color.Color.END))

			
			if userChoice == 1: # Explore
				
				while userChoice != 0 or player.isAlive == True:
					encounter = randint(1, 7)
					if encounter == 1: # Encounter stranger
						print("Stranger says hi")
						sleep(1)
						return

					elif encounter == 2: # Traveling merchant
						print("A merchant has set up shop across the road")
						sleep(1)
						return 
						
					elif encounter == 3: # Find treasure
						print("I found a chest!")
						# player.addinventory("Health Potion")
						# TODO: Properly get player an extra item
						sleep(1)
						return 
						
					elif encounter == 4: # Dungeon time
						print("That cave looks interesting, maybe I should go in")
						sleep(1)
						return 
						
					elif encounter == 5: # Found a Town
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
				# player.displayInventory()
				player.useItem()
				
			elif userChoice == 3: # Player stats
				playerHP = player.getCurrentHP()
				playerTotalHP = player.getMaxHP()
				if playerHP >= playerTotalHP * .75: # Top 75% of hp
					print(color.Color.DARKCYAN + "I'll be fine" + color.Color.END)
				elif playerHP >= playerTotalHP * .50 and playerHP < playerTotalHP * .75: # Between 50 - 75%
					print(color.Color.DARKCYAN + "Some cuts and bruises, I'm otherwise okay" + color.Color.END)
				elif playerHP >= playerTotalHP * .25 and playerHP < playerTotalHP * .50: # Between 25 - 50%
					print(color.Color.DARKCYAN + "I'll need healing soon" + color.Color.END)
				elif playerHP >= playerTotalHP * .1 and playerHP < playerTotalHP * .25: # Between 1-25%
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
			self.displayEnemyStats(opponent)

			userChoice = input(color.Color.RED + f"{opponent.className}: {opponent.catchPhrase}\n\n1. Slap it over the head\n2. Attempt a takedown\n3. Inventory\n4. Flee\n0. Exit\n\nChoice: " + color.Color.END)
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
				# player.displayInventory()
				player.useItem()

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

		if player.isAlive() == True and opponent.isAlive() == False:
			# TODO: Help me work
			# i = Item()
			# i.createBuff()
			# player.addinventory(i)
			print("There's something on the ground")
			# player.addinventory("Health Potion")
			# TODO: Properly give player an item
			player.checklevelUP(opponent.getXP())
			sleep(1)




	# Rewrite me after Enemy class remake
	def displayEnemyStats(self, Enemy): # Show enemy stats
		print(color.Color.DARKCYAN + f'{Enemy.className} - HP: {Enemy.getCurrentHP()}/{Enemy.getMaxHP()}')

	def displayCombatStats(self, player, mana, stamina): # Keep track of current combat stats
		print(color.Color.DARKCYAN + f'{player.className} - HP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {mana}/{player.getMana()} | EN: {stamina}/{player.getStam()}\n' + color.Color.END)
	
	def displayStats(self, player): # For most menus
		print(color.Color.DARKCYAN + f'{player.className}\nHP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {player.getMana()} | XP: {player.getXP()}\n ' + color.Color.END)
	
	def displayFullStats(self, player): # For when user wants/needs to see their total stats
		print(color.Color.DARKCYAN + f'{player.className}\nHP: {player.getCurrentHP()}/{player.getMaxHP()} | MP: {player.getMana()}\nGP: {player.getGP()} | XP: {player.getXP()}\n' + color.Color.END)


