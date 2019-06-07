"""
This module implements the required classes and methods of the game.
It comprises the Player, Card and CardsCollection classes.
"""
import random


class Player(object):
    """
    Simulates a player.
    """

    def __init__(self, name, point=0):
        """
        Initialises a Player instance.
        :param name: player's name
        :param point: player's starting point (default=0)
        """
        self._handsize = 1
        self._godspell = 1
        self._resurrectspell = 1
        self._name = name
        self._point = point
        self._deck = CardsCollection()
        self._hand = CardsCollection()

    @property
    def name(self):
        """
        Player's name getter.
        :return self._name: player's name
        """
        return self._name

    @property
    def point(self):
        """
        Player's Point getter.
        :return self.Point: player's Point value
        """
        return self._point

    @property
    def godspell(self):
        """
        Player's godspell getter.
        :return self._godspell: player's god spell        """
        return self._godspell

    @property
    def resurrectspell(self):
        """
        Player's resurrect spell getter.
        :return self._resurrect spell: player's resurrect spell        """
        return self._resurrectspell

    @property
    def deck(self):
        """
        Player's deck getter.
        :return self._deck: player's deck (a CardsCollection() object)        """
        return self._deck

    @property
    def hand(self):
        """
        Player's hand getter.
        :return self._hand: player's hand (a CardsCollection() object)        """
        return self._hand

    def init_hand(self, deck):
        """
        Initialises player's hand).
        """
        for _ in range(self._handsize):
            if deck.size() == 0:
                print("zero")
            card = deck.pop()
            self._hand.push(card)

    def play_card(self, index, opponent_index, opponent, discard, characteristics):
        """
        :param index: card's index on player's hand
                opponent player object,
                Discard deck to store played card
                Characteristics to test the strength of card
        """
        if index < self._hand.size() and opponent_index < opponent._hand.size():
            card = self._hand.pop(index)
            discard.push(card)
            card_op = opponent._hand.pop(index)
            discard.push(card_op)
            if characteristics == 'S':
                if card.strength > card_op.strength:
                    self._point += 1
                else:
                    opponent._point += 1
            elif characteristics == 'K':
                if card.skill > card_op.skill:
                    self._point += 1
                else:
                    opponent._point += 1
            elif characteristics == 'I':
                if card.size > card_op.size:
                    self._point += 1
                else:
                    opponent._point += 1
            elif characteristics == 'R':
                self._resurrectspell = 0
                card_resurrect = random.randint(1, discard.size())
                card = discard.pop(card_resurrect)
                self._hand.push(card)
            print('\nCard played:\n%s' % card)
        else:
            print('Please enter correct input')


class Card(object):
    """
    Simulates a card.
    """

    def __init__(self, name, strength=0, skill=0, size=0):
        """
        Initialises a Card instance.

        :param name: card's name
        :param strength: card's character attack strength (max 50)
        :param skill: card's character skill(max 50)
        :param size: card's character size (max 50)
        """
        self._name = name
        self._strength = strength
        self._skill = skill
        self._size = size

    @property
    def name(self):
        """
        Card's name getter.
        :return self._name: card's name
        """
        return self._name

    @property
    def strength(self):
        """
        Card's money strength getter.
        :return self._money: card's money strength
        """
        return self._strength

    @property
    def skill(self):
        """
        Card's attack strength getter.
        :return self._attack: card's attack strength
        """
        return self._skill

    @property
    def size(self):
        """
        Card's attack strength getter.
        :return self._attack: card's attack strength
        """
        return self._size

    def __str__(self):
        """
        Called when str method is invoked for a card instance.
        :return: a string that represents card's content
        """
        return 'Name: %s, Strength %s with skill %s and size %s' % \
               (self._name, self._strength, self._skill, self._size)


class CardsCollection(object):
    """
    Simulates a collection of cards.
    """

    def __init__(self):
        """
        Initialises a CardCollection instance.
        """
        self._cards = []

    @property
    def cards(self):
        """
        Cards' list getter.

        :return self._cards: a list of cards
        """
        return self._cards

    def shuffle_collection(self):
        """
        Shuffles collection's cards
        """
        random.shuffle(self._cards)


    def push(self, card, times=1):
        """
        Appends a card to the cards' list (multiple times, i case the
        corresponding parameter is given).

        :param card: the card to be added to the collection (a Card instance)
        :param times, number of identical cards to be added
        """
        self._cards.extend(times * [card])

    def pop(self, index=-1):
        """
        Removes a card from cards' list based on the given index (top card by default).

        :param index: the index of the card to be removed
        """
        return self._cards.pop(index)

    def size(self):
        """
        Returns the size of the cards list

        :return the size of the cards list
        """
        return len(self._cards)

    def print_collection(self, indexes=False):

        """
        Prints the collection's cards (and their indexes, in case the appropriate parameter is set).
         :param indexes: if True the method prints the indexes of the cards as well
         """
        if indexes:
            for i in range(self.size()):
                print("[%s] %s" % (i, self._cards[i]))
        else:
            for i in range(self.size()):
                print(self._cards[i])

    def print_card(self, index=0):
        """
        Prints the card with the given index.

        :param index: the index of the card in the collection
        """
        print(self._cards[index])
