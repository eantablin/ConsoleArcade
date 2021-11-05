import os # Used for clearing the console
import string
import time
from random import randint, choice # Used to select an item from the words dictionary
from dependencies import color, hangmanascii

cls = lambda: os.system('clear') # Clear Console

class HangMan():

    def runGame(self):
        cls()
        userChoice = '1'

        while userChoice != '0':
            userChoice = input(color.Color.BLUE + "Play Hangman?\n1. Game On!\n0. Exit " + color.Color.END)
            try:
                int(userChoice)
                isInt = True
            except ValueError:
                isInt = False
                print(color.Color.RED + "Invalid input, try a number instead." + color.Color.END)
                print(color.Color.RED + "HINT: The only accepted inputs are 1 and 0!" + color.Color.END)
                time.sleep(1.5)
            cls()
            if userChoice == '1':
                self.gameOn()

    def getWord(self):
        words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
        compChoice = choice(words) # Chooses a word from words array
        return compChoice.lower()
    
    def gameOn(self):
        word = self.getWord()
        wordLetters = set(word) # Used to keep track of all the letters in the chosen word
        alphabet = set(string.ascii_lowercase) # Uppercase english letters
        usedLetters = set() # Keeps track of what letters the user has guessed
        chances = 10

        while len(wordLetters) > 0 and chances > 0:
            cls() 
            print(hangmanascii.printHangmanASCII(chances)) # Prints the corresponding Hangman acsii art
            print('')
            print(color.Color.BLUE + "You have " + str(chances) + " incorrect guesses left.\n""You have used these letters: ", " ".join(usedLetters) + color.Color.END) # " ".join(['a', 'b', 'cd']) --> 'a b cd'
            listLetters = [letter if letter in usedLetters else '-' for letter in word] # Current word ie (W - O R D)
            print(color.Color.CYAN + "Current word: ", " ".join(listLetters) + color.Color.END)
            userLetter = input(color.Color.BLUE + "Guess a letter: " + color.Color.END)
            userLetter = userLetter.lower()
            print('')
            if userLetter in alphabet - usedLetters:
                usedLetters.add(userLetter)
                # TODO
                # usedLetters = sorted(usedLetters)
                if userLetter in wordLetters:
                    wordLetters.remove(userLetter)
                else:
                    chances -= 1 # If user guesses incorrectly, they lose a guess chance
                    print(color.Color.RED + "Letter is not in word!" + color.Color.END)
                    time.sleep(1)
            elif userLetter in usedLetters:
                print(color.Color.BLUE + "You have already used that letter." + color.Color.END)
                time.sleep(1)

            else:
                print(color.Color.BLUE + "Invalid selection." + color.Color.END)
                time.sleep(1)
        if chances == 0:
            print(color.Color.RED + hangmanascii.hangmanL + color.Color.END) # Prints the corresponding Hangman ascii art
            print('')
            print(color.Color.RED + "You have lost. The correct word was, " + word + "."+ color.Color.END)
        else:
            print(hangmanascii.hangmanW) # Prints the corresponding Hangman acsii art
            print('')
            print(color.Color.BLUE + "You have guessed the word, " + word +", correctly!"+ color.Color.END)