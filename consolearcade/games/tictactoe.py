import os
import math 
import time
from random import choice
from dependencies import color

cls = lambda: os.system('clear') # Clear Console

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Used for 3 * 3 TicTacToe board
        self.currentWinner = None # Keep track of who has won
    
    def printBoard(self): # Will be used to print a 3 * 3 TicTacToe board
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]: # Break up into groups of 3 spaces
            print('| ' + ' | '.join(row) + ' |')

    def clearBoard(self): # Used to clear the game board and reset the currentWinner after a game
        self.board = [' ' for _ in range(9)]
        self.currentWinner = None

    @staticmethod # Used because there is no need to pass in self
    def printBoardNums():
        """
        | 0 | 1 | 2 |
        | 3 | 4 | 5 |
        | 6 | 7 | 8 |
        """
        numberBoard = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)] # Give indices of what number is in what row
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')

    def availableMoves(self): # Returns a list of the available (unused) spaces
        moves = []
        for (i, space) in enumerate(self.board): # Ex: [(0, ' '), (1, 'x'), (2, 'o')]
            if space == ' ':
                moves.append(i)
        return moves

    def emptySquares(self):
        return ' ' in self.board

    def numEmptySquares(self):
        return len(self.availableMoves())
    
    def makeMove(self, square, letter):
        # Need to check if it's a valid move, if so return True else False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Winner if there is a row of the same letter
        # Check for row win
        rowIndex = square // 3
        row = self.board[rowIndex * 3: (rowIndex + 1) * 3]
        if all([spot == letter for spot in row]): # Checks for three of the same letter in a row
            return True
        
        # Check for column win
        colIndex = square % 3
        column = [self.board[colIndex + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]): # Checks for three of the same letter in a column
            return True

        # Check for diagonal win (can only be even numbered positions (0, 2, 4, 6, 8))
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]): # Checks for three of the same letter in diagonal1
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]): # Checks for three of the same letter in diagonal2
                return True
        
        # If no winner
        return False

    def play(self, game, xPlayer, oPlayer, printGame = True):
        if printGame:
            self.printBoardNums()
    
        letter = 'X' # First player is x

        while self.emptySquares():
        # Get moves from the two players
            if letter == 'O':
                square = oPlayer.getMove(game)
            else:
                square = xPlayer.getMove(game)

            if self.makeMove(square, letter):
                if printGame:
                    cls()
                    print(letter + f" makes a move to square {square}")
                    self.printBoard()
                    print('')
            
            if self.currentWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter
            # Switch Players
            letter = 'O' if letter == 'X' else 'X'
    
            time.sleep(1.5)

        if printGame:
            print("It's a tie!")


    def runGame(self):
        cls()
        userChoice = 1
        while userChoice != 0:
            userChoice = input("Play Tic-Tac-Toe?\n1. Play\n0. Exit ")
            try:
                userChoice = int(userChoice)
                isInt = True
            except ValueError:
                isInt = False
                print(color.Color.RED + "Invalid input, try a number instead." + color.Color.END)
                print(color.Color.RED + "HINT: The only valid inputs are 1 and 0!" + color.Color.END)
                time.sleep(1.5)
            cls()
            if userChoice == 1:
                TicTacToe.clearBoard(self)
                xPlayer = HumanPlayer('X')
                oPlayer = ComputerPlayer('O')
                t = TicTacToe()
                TicTacToe.play(self, t, xPlayer, oPlayer, printGame = True)

class Player():
    def __init__(self, letter): # Letter: x or o
        self.letter = letter
    
    def getMove(self, game): # Allow players to get their next move
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = choice(TicTacToe.availableMoves(game)) # Selects a random available space for ComputerPlayer
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            validMoves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
            if square in validMoves:
                val = int(square)
            if val not in game.availableMoves():
                print("Invalid square, try again.")
            else:
                validSquare = True
        return val