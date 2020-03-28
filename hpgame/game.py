'''
The main game of the harry potter.
'''

class Game:
    def __init__(self, heroes: list):
        '''
        Initialize the game.
            
        self.heroes[0] is the active hero.
        '''
    # TODO: directly init dark_events/locations/villains
    # (that would require a game 1,2,3...,7 library),
    # or pass them as params?
        self.heroes = heroes
        # TODO: more to init

    def start(self):
        '''
        Starts the game.
        '''
        self.start_turn()

    def start_turn(self):
        # TODO
        pass

    def end_turn(self):
        # TODO
        self.heroes.append(self.heroes.pop(0))

    def discard_card(self, target):
        '''
        The target hero discards a card.
        '''
        # TODO
        pass

    def gain_hp(self, target, amount):
        # TODO
        pass

    def lose_hp(self, target, amount):
        # TODO
        pass

    def active_hero(self):
        '''
        Returns the current active hero.
        '''
        return self.heroes[0]
