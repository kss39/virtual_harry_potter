"""
States is a collection of functions to resolve certain actions
when game reaches specific states. These states can invoke each
other, causing a chain reaction.
"""

from game import Game

def start_turn(game: Game):
    """
    The start of a hero's turn.
    Steps:
    - reveal and resolve dark arts
    - resolve villain
    - # TODO: play cards
    """
    # TODO: rotate to a new hero.
    game.reveal_dark_arts()
    for v in game.villains:
        reaction = getattr(v, 'start_turn', None)
        if callable(reaction):
            reaction(game)
    # TODO: the hero stars to play.
    # TODO: the hero ends.
    end_turn(game)

def end_turn(game):
    pass

def discard_card(game, count):
    pass

def gain_hp(game, target, amount):
    pass

def lose_hp(game, target, amount):
    pass

def attack_villain(game, damage):
    pass

def villain_on_kill(game):
    pass

def location_lose(game):
    pass

def control_add(game):
    pass

def control_remove(game):
    pass
