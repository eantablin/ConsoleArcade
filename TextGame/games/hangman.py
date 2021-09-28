import os # Used for clearing the console
import string
from random import randint, choice # Used to select an item from the words dictionary
from dependencies import color

cls = lambda: os.system('clear') # Clear Console

class HangMan():

    def runGame(self):
        cls()
        userChoice = 1

        while userChoice != 0:
            userChoice = int(input(color.Color.BLUE + "Play Hangman?\n1. Game On!\n0. Exit" + color.Color.END))
            cls()
            if userChoice == 1:
                self.gameOn()

    def getWord(self):
        words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
        compChoice = choice(words) # Chooses a word from words array
        return compChoice.upper()
    
    def gameOn(self):
        word = self.getWord()
        wordLetters = set(word) # Used to keep track of all the letters in the chosen word
        alphabet = set(string.ascii_uppercase) # Uppercase english letters
        usedLetters = set() # Keeps track of what letters the user has guessed

        while len(wordLetters) > 0: 
            userLetter = input(color.Color.BLUE + "Guess a letter: " + color.Color.END)
            userLetter.upper()
            if userLetter in alphabet - usedLetters:
                usedLetters.add(userLetter)
                if userLetter in wordLetters:
                    wordLetters.remove(userLetter)
            elif userLetter in usedLetters:
                print(color.Color.BLUE + "You have already used that letter." + color.Color.END)
            else:
                print(color.Color.BLUE + "Invalid selection." + color.Color.END)
