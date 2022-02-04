from random import randint


class Item:
    name = ""  # Item name
    price = 0  # Item price
    attribute = ""  # Item type
    rarity = ""  # Common, Rare, Heroic, Legendary
    description = ""  # Item lore/characteristics
    healthRegen = 0  # Direct healing
    healthOverTime = 0  # Heal over Time, HoT
    manaRegen = 0  # Mana intake
    manaOverTime = 0  # Mana intake over time, to prevent spell spamming, most common
    autoDamage = 0  # Damage taken by using item
    autoDamageOverTime = 0  # Damage taken by using item, over time
    damage = 0  # Damage increase
    damageOverTime = 0  # Attacks apply a DoT
    canCook = False  # Can item be cooked? # TODO: Properly implement me later

    def items(self):
        itemsList = [
            "Health Potion",
            "Apples",
            "Tomatoes",
            "Soup",
            "Mana Potion",
            "Small Health Potion",
            "Small Mana Potion",
            "Cursed Mirror",
            "Strange Doll",
            "Screaming Head",
            "Death's Cloak",
            "Rock",
            "Rotten Tomato",
            "Jar of Nails",
            "Sand",
            "Cute Plushie",
            "Knife",
            "Longsword",
            "Whip",
            "Wand",
            "Magic Scroll",
        ]

    def createBuff(self):  # Advantageous items to have
        ranNum = randint(1, 100)
        self.attribute = "buff"

        if ranNum <= 10:  # Health Potion, 10% chance
            self.name = "Health Potion"
            self.price = 20
            self.rarity = "Common"
            self.healthRegen = 20
            self.description = "This bottle has some heft to it, and a pungent smell"
            self.canCook = False
        elif ranNum <= 30 and ranNum > 10:  # Apples, 20% chance
            self.name = "Apples"
            self.price = 5
            self.rarity = "Common"
            self.healthRegen = 5
            self.description = "Red, crispy apple"
            self.canCook = True
        elif ranNum <= 50 and ranNum > 30:  # Tomatoes, 20% chance
            self.name = "Tomatoes"
            self.price = 5
            self.rarity = "Common"
            self.description = "Red, juicy tomato"
            self.canCook = True
        elif ranNum <= 80 and ranNum > 50:  # Soup, 30% chance
            self.name = "Soup"
            self.price = 10
            self.rarity = "Common"
            self.healthRegen = 10
            self.description = (
                "A hearty soup stored in a jar, maybe it'd taste better cooked?"
            )
            self.canCook = True
        elif ranNum <= 85 and ranNum > 80:  # Mana potion, 5% chance
            self.name = "Mana Potion"
            self.price = 30
            self.rarity = "Common"
            self.manaRegen = 20
            self.description = "Blue viscous liquid, is it looking at me?"
            self.canCook = False
        elif ranNum <= 90 and ranNum > 85:  # Small Health Potion, 5% chance
            self.name = "Small Health Potion"
            self.price = 10
            self.rarity = "Common"
            self.healthRegen = 15
            self.description = "Red tones in a small bottle, better not drop it"
            self.canCook = False
        elif ranNum <= 100 and ranNum > 90:  # Small Mana Potion, 10% chance
            self.name = "Small Mana Potion"
            self.price = 15
            self.rarity = "Common"
            self.manaRegen = 10
            self.description = "Blue tones in an oddly shaped triangular bottle"
            self.canCook = False

    def createDebuff(self):  # Items that you might not want to use
        ranNum = randint(1, 100)
        self.attribute = "debuff"

        # TODO: Cursed mirror seems like a buff/equipment
        if ranNum <= 25:  # Cursed Mirror, 25% chance
            self.name = "Cursed Mirror"
            self.price = 10
            self.rarity = "Common"
            self.description = (
                "A black mirror, reflects a portion of the damage you deal"
            )
            self.canCook = False
        elif ranNum <= 50 and ranNum > 25:  # Strange Doll, 25% chance
            self.name = "Strange Doll"
            self.price = 5
            self.rarity = "Common"
            self.description = (
                "Something is off about this doll... It creates an ominous atmosphere"
            )
            self.canCook = False
        elif ranNum <= 75 and ranNum > 50:  # Screaming Head, 25% chance
            self.name = "Screaming Head"
            self.price = 5
            self.rarity = "Common"
            self.description = "A severed, bloody head. It will not stop wailing."
            self.canCook = False
        elif ranNum <= 100 and ranNum > 75:  # Death's Cloak , 25% chance
            self.name = "Death's Cloak"
            self.price = 20
            self.rarity = "Rare"
            self.description = "Someone stole this cloak from the physical embodiment of Death... It will attract his attention if you wear it."
            self.canCook = False

    def createJunk(self):  # Items which have little value aside from monetary
        ranNum = randint(1, 100)
        self.attribute = "junk"

        if ranNum <= 20:  # Rock, 20% chance
            self.name = "Rock"
            self.price = 1
            self.rarity = "Common"
            self.autoDamage = 5
            self.description = "Just a rock, has sharp edges"
            self.canCook = False
        elif ranNum <= 40 and ranNum > 20:  # Rotten Tomato, 20% chance
            self.name = "Rotten Tomato"
            self.price = 5
            self.rarity = "Common"
            self.autoDamage = 2
            self.description = "Smells bad, might burst if handled incorrectly"
            self.canCook = False
        elif ranNum <= 60 and ranNum > 40:  # Jar of Nails, 20% chance
            self.name = "Jar of Nails"
            self.price = 10
            self.rarity = "Common"
            self.autoDamageOverTime = 5
            self.description = "A jar full of rusty nails, could give someone Tetanus"
            self.canCook = False
        elif ranNum <= 80 and ranNum > 60:  # Sand, 20% chance
            self.name = "Sand"
            self.price = 5
            self.rarity = "Common"
            self.autoDamage = 2
            self.description = "A small pouch of sand, will break open if thrown."
            self.canCook = False
        elif ranNum <= 100 and ranNum > 80:  # Cute Plushie, 20% chance
            self.name = "Cute Plushie"
            self.price = 10
            self.rarity = "Rare"
            self.description = "A small plush toy, will provide moral support and hugs."
            self.canCook = False

    def createEquipment(
        self,
    ):  # Items player can equip for N amount of combat scenarios
        ranNum = randint(1, 100)
        self.attribute = "equipment"

        if ranNum <= 30:  # Knife, 30% chance
            self.name = "Knife"
            self.price = 15
            self.rarity = "Common"
            self.autoDamage = 7
            self.description = "A very sharp knife"
            self.canCook = False
        elif ranNum <= 50 and ranNum > 30:  # Longsword, 20% chance
            self.name = "Longsword"
            self.price = 20
            self.rarity = "Common"
            self.autoDamage = 10
            self.description = "A princely weapon, it should serve well"
            self.canCook = False
        elif ranNum <= 70 and ranNum > 50:  # Whip, 20% chance
            self.name = "Whip"
            self.price = 10
            self.rarity = "Common"
            self.autoDamage = 5
            self.description = "A spiked whip"
            self.canCook = False
        elif ranNum <= 90 and ranNum > 70:  # Wand, 20% chance
            self.name = "Wand"
            self.price = 5
            self.rarity = "Common"
            self.autoDamage = 10
            self.description = "The weapon of a witch or wizard"
            self.canCook = False
        elif ranNum <= 100 and ranNum > 90:  # Magic Scroll, 10% chance
            self.name = "Magic Scroll"
            self.price = 20
            self.rarity = "Rare"
            self.manaOverTime = 2
            self.description = "Can increase a persons' mana"
            self.canCook = False
