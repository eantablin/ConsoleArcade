import os
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

			# Test if items work
			# it = Item()
			# it.createBuff()
			# self.addinventory(it)

			# Hold current inventory and it's size
			inventory = self.getinventory()
			inventoryLength = len(inventory)

			counter = 1 # Display items from 1..N, skipping 0 due to exit condition

			if inventoryLength > 0: # If there's something in inventory
				for i in inventory: # Loop through it's entirety
					print(color.Color.DARKCYAN + f"{counter}) {i.name}" + color.Color.END) # Output each slot
					counter += 1 # Increase reference value by 1

				print(color.Color.DARKCYAN + "0) Exit\n" + color.Color.END)

			else: # Empty satchel, break out of loop
				print("My satchel is empty.")
				sleep(1)
				break
				
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

	
	def isAlive(self):
		if self.currentHP > 0:
			return True
		else:
			return False
			
	# Getters and setters
	
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

	# Currently not being used
	def removeinventory(self, itemToRemove): # self, value to remove
		# TODO: OPTIMIZE ME!
		counter = 0
		for i in self.inventory:
			if i == itemToRemove:
				self.inventory.remove(i)
				return
			counter += 1
