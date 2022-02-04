""" Empty Gallows
  ____________
     |/     
     |      
     |      
     |      
     |      
     |
    _|___
"""
""" Completed Hangman
  ____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
"""
""" Win
  ____________
     |/      
     |      
     |       _
     |      (_)
     |      \|/
     |       |
    _|___   / \
"""
""" Lose
  ____________
     |/      |
     |       |
     |      (_)
     |      \|/
     |       |
     |      / \
    _|___
"""
hangman1 = "____________\n |/      |\n |      (_)\n |      \|/\n |       |\n |      / \ \n |\n_|___"
hangman2 = "____________\n |/      |\n |      (_)\n |      \|/\n |       |\n |      /   \n |\n_|___"
hangman3 = "____________\n |/      |\n |      (_)\n |      \|/\n |       |\n |          \n |\n_|___"
hangman4 = "____________\n |/      |\n |      (_)\n |      \|/\n |        \n |          \n |\n_|___"
hangman5 = "____________\n |/      |\n |      (_)\n |      \| \n |        \n |          \n |\n_|___"
hangman6 = "____________\n |/      |\n |      (_)\n |       | \n |        \n |          \n |\n_|___"
hangman7 = "____________\n |/      |\n |      (_)\n |         \n |        \n |          \n |\n_|___"
hangman8 = "____________\n |/      |\n |      ( )\n |         \n |        \n |          \n |\n_|___"
hangman9 = "____________\n |/      |\n |         \n |         \n |        \n |        \n | \n_|___"
hangman10 = "____________\n |/       \n |         \n |         \n |        \n |        \n | \n_|___"
hangmanL = "____________\n |/      |\n |       |\n |      (_)\n |      \|/\n |       | \n |      / \ \n_|___"
hangmanW = "____________\n |/       \n |         \n |       _ \n |      (_)\n |      \|/\n |       | \n_|___   / \ "


def printHangmanASCII(chances):
    if chances == 10:
        return hangman10
    elif chances == 9:
        return hangman9
    elif chances == 8:
        return hangman8
    elif chances == 7:
        return hangman7
    elif chances == 6:
        return hangman6
    elif chances == 5:
        return hangman5
    elif chances == 4:
        return hangman4
    elif chances == 3:
        return hangman3
    elif chances == 2:
        return hangman2
    elif chances == 1:
        return hangman1
    else:
        print("")
