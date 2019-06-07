"""
This module implements the game's logic and is used to play to game.
"""

import random
from deckgame.helper import Player, CardsCollection, Card


class Game(object):
    """
    Simulates a game. This is the main class of the game.
    """
    def __init__(self):
        """
        Initialises the game by adding new players,
        Two Decks: 1st for whole cards
                   2nd for only used / played cards
        start used for who starts first
        """
        self.player_1 = Player('Player 1')
        self.player_2 = Player('Player PC')
        self.deck = CardsCollection()
        self.discard = CardsCollection()
        self.start = True

    def start_game(self):
        """
        This is the main method of the game. It plays the game until a winner
        is identified.
        """
        self.set_up_game()
        self.start = self.get_opponent()


        # player_selection = input('Please select 1. 1 player \n2. 2 Players')
        # if player_selection == '2':
        #     for _ in range(self.deck.size()-1):
        #         self.player_1_turn()
        #         self.player_2_turn()

        winner = False
        while not winner:
            if self.start:
                self.player_1_turn()
                self.display_info()
                winner = self.check_winner()

            else:
                self.player_2_turn()
                self.display_info()
                winner = self.check_winner()

    @staticmethod
    def get_opponent():
        """
        Simulating dice throws and whoever gets higher number will start the game.
        """
        player_1_dice = random.randint(1, 6)
        print("\nPlayer 1 dice score" + str(player_1_dice))
        player_2_dice = random.randint(1, 6)
        print("\nPlayer 2 dice score" + str(player_2_dice))

        if player_1_dice >= player_2_dice:
            print('Player 1 will start the game')
            return True
        else:
            print('Player 2 will start the game')
            return False

    def set_up_game(self):
        """
        Initialises the game by generating the decks,
         Distributing equal numbers of the card randomly to players.
        """
        self.init_central_deck()
        self.deck.shuffle_collection()
        self.player_1._handsize = int(self.deck.size() / 2)
        self.player_2._handsize = int(self.deck.size() / 2)
        self.player_1.init_hand(self.deck)
        self.player_2.init_hand(self.deck)

    def init_central_deck(self):
        """
        Initialises the central deck by pushing the predefined cards into the
        deck.
        format (Name,Strength, Skill, Size)
        """
        self.deck.push(Card('Iron Man', 30, 45, 35))
        self.deck.push(Card('Hulk', 50, 10, 50))
        self.deck.push(Card('Groot', 40, 19, 48))
        self.deck.push(Card('Thanos', 45, 30, 46))
        self.deck.push(Card('Thor', 35, 25, 36))
        self.deck.push(Card('Ultron', 33, 48, 38))
        self.deck.push(Card('Captain-America', 36, 42, 33))
        self.deck.push(Card('Spider-man', 26, 50, 26))
        self.deck.push(Card('Vision', 28, 24, 28))
        self.deck.push(Card('Star-lord', 18, 32, 27))

    def display_info(self):
        """
        Displays player's Standings.
        """

        print("|----------------- INFO -----------------|")
        print("Displays player's Standings point:")
        print('You: %s' % self.player_1.point)
        print('PC: %s' % self.player_2.point)
        print('----------------------------------------')

    def player_1_turn(self):
        """
        This method is responsible for player's (player_1) turn. It asks for
        the action to be taken by printing appropriate messages indicating the
        valid options and calls the corresponding methods.
        """
        while True:
            self.display_info()
            print("\n----------------------------------------")

            if self.player_1.hand.size() > 0:
                self.player_1.hand.print_card(-1)
                print("Choose Action: (S = Strength, K = skill, I = size, G = God, R=Resurrect)")
                valid = ['S', 'K', 'I', 'G', 'R']
                self.player_1_action(valid)
            else:
                print("\nNo more possible actions.\nTurn ending.")
                break

    def player_1_action(self, valid):
        """
        Gets user's choice, validates it and calls the appropriate method to
        complete the action.

        :param valid: a list of valid options for user's input
        :return True: if user decides to end his turn (False otherwise)
        """
        action = input("Enter Action: ")
        if action not in valid:
            print("\nPlease give a valid option!")
        elif action == 'S':
            self.player_1.play_card(-1,-1, self.player_2, self.discard, action)
        elif action == 'K':
            self.player_1.play_card(-1,-1, self.player_2, self.discard, action)
        elif action == 'I':
            self.player_1.play_card(-1,-1, self.player_2, self.discard, action)
        elif action == 'G':
            if self.player_1._godspell == 1:
                op_index = int(input('Please mention which card opponent should play ?'))
                index = int(input('Please mention which card you want to play ?'))
                self.player_1.hand.print_card(index)
                print("Choose Action: (S = Strength, K = skill, I = size, R=Resurrect)")
                characteristics = input('please enter')
                self.player_1.play_card(index, op_index, self.player_1,self.discard, characteristics)
                self.player_1._godspell = 0
            elif self.player_1._godspell > 1 or self.player_1._godspell < 1:
                print('You already played God spell or wrong selection')

        elif action == 'R':
            if self.player_1._resurrectspell == 1:
                player_resurrect = random.randint(1, self.discard.size()-1)
                card = self.discard.pop(player_resurrect)
                self.player_1.hand.push(card)
                self.player_1._resurrectspell = 0
                self.player_1_turn()
                # self.player_1.play_card(-1,-1, self.player_2, self.discard)

            elif self.player_1._godspell > 1 or self.player_1._godspell < 1:
                print('You already played Resurrect spell or wrong selection')
            return True
        return False

    def player_2_turn(self):
        """
        This method is responsible for player's (player_2) turn. It asks for
        the action to be taken by printing appropriate messages indicating the
        valid options and calls the corresponding methods.
        """
        while True:
            self.display_info()
            print("\n----------------------------------------")

            if self.player_2.hand.size() > 0:
                self.player_2.hand.print_card(-1)
                print("Choose Action: (S = Strength, K = skill, I = size, G = God, R=Resurrect)")
                valid = ['S', 'K', 'I', 'G', 'R']
                self.player_2_action(valid)
            else:
                print("\nNo more possible actions.\nTurn ending.")
                break

    def player_2_action(self, valid):
        """
        Gets user's choice, validates it and calls the appropriate method to
        complete the action.

        :param valid: a list of valid options for user's input
        :return True: if user decides to end his turn (False otherwise)
        """
        action = input("Enter Action: ")
        if action not in valid:
            print("\nPlease give a valid option!")
        elif action == 'S':
            self.player_2.play_card(-1,-1, self.player_1, self.discard, action)
        elif action == 'K':
            self.player_2.play_card(-1,-1, self.player_1, self.discard, action)
        elif action == 'I':
            self.player_2.play_card(-1,-1, self.player_1, self.discard, action)
        elif action == 'G':
            if self.player_2._godspell == 1:
                op_index = int(input('Please mention which card opponent should play ?'))
                index = int(input('Please mention which card you want to play ?'))
                self.player_2.hand.print_card(index)
                print("Choose Action: (S = Strength, K = skill, I = size, R=Resurrect)")
                characteristics = input('please enter')
                self.player_2.play_card(index, op_index, self.player_1,self.discard, characteristics)
                self.player_2._godspell = 0
            elif self.player_2._godspell > 1 or self.player_2._godspell < 1:
                print('You already played God spell or wrong selection')

        elif action == 'R':
            if self.player_2._resurrectspell == 1:
                player_resurrect = random.randint(1, self.discard.size()-1)
                card = self.discard.pop(player_resurrect)
                self.player_2.hand.push(card)
                self.player_2._resurrectspell = 0
                self.player_2_turn()
                # self.player_1.play_card(-1,-1, self.player_2, self.discard)

            else:
                print('You already played Resurrect spell or wrong selection')
            return True
        return False

    def check_winner(self):
        """
        Check whether there is a winner, based on players' health, strength
        and on central deck's size.

        :return winner: True if a winner has been found
        """
        winner = False
        if self.deck.size() == 0:
            print("No more cards available")
            if self.player_1.point > self.player_2.point:
                winner = True
                print("Player One Wins")
            elif self.player_1.point == self.player_2.point:
                winner = True
                print("Draw")
            elif self.player_1.point < self.player_2.point:
                winner = True
                print("Computer Wins")

            winner = True
        return winner
