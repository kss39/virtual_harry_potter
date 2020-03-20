import cards

class Hero:
    def __init__(self, hp=10):
        self.hp = hp
        self.money = 0
        self.deck = [cards.alohomora * 7]

class Harry(Hero):
    def __init__(self, hp=10):
        super(hp)
        self.deck.append(cards.hedwig)
        self.deck.append(cards.firebolt)
