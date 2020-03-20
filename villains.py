from game import Game
import states

class Villain:
    def __init__(self, hp):
        self.hp = hp

class QuirinusQuirrel(Villain):
    """
    Active Hero loses 1 hp.

    Reward:
    All heroes gain $1 and 1 hp.
    """
    def start_turn(self, game: Game):
        states.lose_hp(game, 1)
