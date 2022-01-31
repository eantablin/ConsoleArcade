import os
from random import randint, choice, shuffle
from dependencies import color
from time import sleep

cls = lambda: os.system('clear') # Clear Console


class Blackjack():
    score = 0
    deck = [2,3,4,5,6,7,8,9,10,11,12,13,14] * 4 # 4 decks
    isAlive = True


    def runGame(self):
        # sleep(2)

        # Initializes hands
        player = self.deal()
        dealer = self.deal() 

        while(self.isAlive):
            cls()
            print("Horse's blackjack! House plays safe at 16")
            self.displayStats(player, dealer)

            uInput = input("(H)it or (S)tay? or (0) to exit: ")

            if "h" in uInput.lower():
                self.hit(player)
                self.checkstats(player, dealer)
            elif "0" or "e" or "x" in uInput.lower():
                self.isAlive = False
            else:
                while sum(dealer) < 17:
                    self.hit(dealer)
                    self.checkstats(player, dealer)

        # if playAgain == True, deck = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 # 4 decks

    def deal(self):
        hand = []

        for i in range(2):
            shuffle(self.deck)
            card = self.deck.pop()

            if card == 11: # A, for now holds 1; make it so player can pick between 1 and 11
                card = 1
            elif card == 12: # J
                card = 10
            elif card == 13: # Q
                card = 10
            elif card == 14: # K
                card = 10

            hand.append(card)
    
        return hand

    # Takes object's hand, adds a card
    def hit(self, hand):
        shuffle(self.deck)
        card = self.deck.pop()

        if card == 11: # A, for now holds 1; make it so player can pick between 1 and 11
            card = 1
        elif card == 12: # J
            card = 10
        elif card == 13: # Q
            card = 10
        elif card == 14: # K
            card = 10

        hand.append(card)

        return hand

    def checkstats(self, player, dealer):
        playerTotal = sum(player)
        dealerTotal = sum(dealer)

        if playerTotal > 21:
            print("Haha, gimme that money")
            
        elif dealerTotal > 21:
            print("Horse cries, busted it's hoof")
            self.score += 1 # unused
        
        


    def displayStats(self, player, dealer):
        playerTotal = sum(player)
        dealerTotal = sum(dealer)

        print(f"Player: {playerTotal}\nDealer: {dealerTotal}")
