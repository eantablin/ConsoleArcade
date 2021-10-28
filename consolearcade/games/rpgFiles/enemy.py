from . import player

class Enemy(player.Player):

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
