'''
A deck contains two card piles: the draw pile and the discard pile.
When the client "draw" a card, it returns the top card on the draw pile;
and when the draw pile doesn't contain a card, all cards in the discard pile
is moved into the draw pile and the draw pile is then reshuffled.

There are several types of deck in the harry potter game, hence every
kind of deck is a subclass of the abstract class Deck.
'''
import random

class Deck:
    '''
    The abstract class Deck.
    '''
    def __init__(self, pile: list):
        '''
        Initialize the deck with the given pile of cards.
        Note that the deck is then responsible for the pile list.
        '''
        self.draw = pile
        random.shuffle(self.draw)
        self.discard = []

    def draw_card(self):
        '''
        the abstract class' draw_card() method deals with the
        situation when the draw pile is empty. All subclasses
        should call super().draw_card() before actually drawing
        cards.
        '''
        if len(self.draw) == 0:
            if len(self.discard) == 0:
                return None
            self.draw = self.discard
            self.discard = []

class DarkEventsDeck(Deck):
    def draw_card(self):
        '''
        Draw a dark event card.
        Return the card as well as put the card into the discard pile.
        '''
        super().draw_card()
        res = self.draw.pop(0)
        self.discard.append(res)
        return res

class HandDeck(Deck):
    '''
    HandDeck is the deck for a hero. It not only contains the draw
    pile and the discard pile; it also has the hand.

    The client can "play" cards in the hand and then the card will
    be put into the discard pile.
    '''
    def __init__(self, pile: list):
        super(pile)
        self.hand = self.draw[0:5]
        self.draw = self.draw[5:]

    def draw_card(self):
        '''
        Draw a Hogwarts! card.
        Put the card into the your hand.
        '''
        super().draw_card()
        self.hand.append(self.draw.pop(0))

class ShopDeck(Deck):
    '''
    The ShopDeck (basically) won't have the discard pile.
    The cards go to the discard pile when a refreshing shop
    is happened.

    6 cards will be put on "on_sale".
    '''
    def __init__(self, pile: list):
        super(pile)
        self.on_sale = self.draw[0:6]
        self.draw = self.draw[6:]

    def draw_card(self):
        '''
        Put a new shop card onto "on_sale".
        '''
        super().draw_card()
        self.on_sale.append(self.draw.pop(0))
