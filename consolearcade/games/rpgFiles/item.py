class Item():
	name = "" # Item name
	price = 0 # Item price
	attribute = "" # Item type
	rarity = "" # Common, Rare, Heroic, Legendary
	description = "" # Item lore/characteristics
	healthRegen = 0 # Direct healing
	healthOverTime = 0 # Heal over Time, HoT
	manaRegen = 0 # Mana intake
	manaOverTime = 0 # Mana intake over time, to prevent spell spamming, most common
	autoDamage = 0 # Damage taken by using item
	autoDamageOverTime = 0 # Damage taken by using item, over time
	damage = 0 # Damage increase
	damageOverTime = 0 # Attacks apply a DoT
	canCook = False # Can item be cooked? # TODO: Properly implement me later

	def items(self):
		itemsList = ["Health Potion", "Apples", "Soup", "Mana Potion", "Small Health Potion", "Small Mana Potion"]

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
	