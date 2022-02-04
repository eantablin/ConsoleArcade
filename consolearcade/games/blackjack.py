import os
from random import randint, choice, shuffle
from dependencies import color
from time import sleep

cls = lambda: os.system("clear")  # Clear Console


class Blackjack:
    score = 0
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4  # 4 decks
    isAlive = True

    def runGame(self):
        # sleep(2)

        # Initializes hands
        player = self.deal()
        dealer = self.deal()

        while self.isAlive:
            cls()
            playerStayed = False
            houseStayed = False  # Placeholder until we implement workaround
            print("Horse's blackjack! House plays safe at 16\n")
            self.displayStats(player, dealer)

            uInput = input("1) Hit\n2) Stay\n0) Exit\n\nChoice: ")

            try:
                uInput = int(uInput)
                # isInt = True
            except ValueError:
                # isInt = False
                print(
                    color.Color.RED
                    + "Invalid input, try a number instead."
                    + color.Color.END
                )
                print(
                    color.Color.RED
                    + "HINT: The only accepted inputs are 1, 2, and 0!"
                    + color.Color.END
                )

            if uInput == 1:
                self.hit(player)
            elif uInput == 2:
                while sum(dealer) < 17:
                    self.hit(dealer)

                houseStayed = True
                playerStayed = True
            elif uInput == 0:
                self.isAlive = False

            player, dealer, self.deck = self.checkstats(
                player, dealer, self.deck, playerStayed
            )

    def deal(self):
        hand = []

        for i in range(2):
            shuffle(self.deck)
            card = self.deck.pop()

            if (
                card == 11
            ):  # A, for now holds 1; make it so player can pick between 1 and 11
                card = 1
            elif card == 12:  # J
                card = 10
            elif card == 13:  # Q
                card = 10
            elif card == 14:  # K
                card = 10

            hand.append(card)

        return hand

    # Takes object's hand, adds a card
    def hit(self, hand):
        shuffle(self.deck)
        card = self.deck.pop()

        if (
            card == 11
        ):  # A, for now holds 1; make it so player can pick between 1 and 11
            card = 1
        elif card == 12:  # J
            card = 10
        elif card == 13:  # Q
            card = 10
        elif card == 14:  # K
            card = 10

        hand.append(card)

        return hand

    def checkstats(self, player, dealer, deck, playerStayed):
        playerTotal = sum(player)
        dealerTotal = sum(dealer)
        uInput = ""

        # Dealer win condition, should have higher odds of player cuz it won't start drawing until player is done
        if playerTotal > 21 or (
            playerTotal <= dealerTotal and playerStayed == True and dealerTotal < 22
        ):

            while uInput not in [1, 2, 0]:
                cls()
                print(
                    f"House wins\n\nPlayer: {playerTotal} | {player}\nDealer: {dealerTotal} | {dealer}\n"
                )
                uInput = input("Play again?\n1) Yes\n2) No\n0) Exit\n\nChoice: ")

                try:
                    uInput = int(uInput)
                except ValueError:
                    print(
                        color.Color.RED
                        + "Invalid input, try a number instead."
                        + color.Color.END
                    )
                    print(
                        color.Color.RED
                        + "HINT: The only accepted inputs are 1, 2, and 0!"
                        + color.Color.END
                    )

                if uInput == 1:
                    return (
                        self.deal(),
                        self.deal(),
                        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4,
                    )

                if uInput == 2 or uInput == 0:
                    self.isAlive = False

        # Player win conditions, higher odds of losing so try to play it safe
        elif (
            playerTotal == 21
            or playerTotal > dealerTotal
            and playerStayed
            or playerTotal < 22
            and playerStayed
        ):

            while uInput not in [1, 2, 0]:
                cls()
                print(
                    f"Player wins\n\nPlayer: {playerTotal} | {player}\nDealer: {dealerTotal} | {dealer}\n"
                )
                self.score += 1
                uInput = input("Play again?\n1) Yes\n2) No\n0) Exit\n\nChoice: ")

                try:
                    uInput = int(uInput)
                except ValueError:
                    print(
                        color.Color.RED
                        + "Invalid input, try a number instead."
                        + color.Color.END
                    )
                    print(
                        color.Color.RED
                        + "HINT: The only accepted inputs are 1, 2, and 0!"
                        + color.Color.END
                    )

                if uInput == 1:
                    return (
                        self.deal(),
                        self.deal(),
                        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4,
                    )

                if uInput == 2 or uInput == 0:
                    self.isAlive = False

        return player, dealer, deck

    def displayStats(self, player, dealer):
        playerTotal = sum(player)
        dealerTotal = sum(dealer)

        # player and dealer are there for demonstration purposes, make them prettier!
        print(f"Player: {playerTotal} | {player}\nDealer: {dealerTotal} | {dealer}\n")
