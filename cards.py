import states
import interact

def alohomora(game, hero):
    """
    Gain $1.
    """
    hero.money += 1

def default_ally(game, hero):
    """
    Gain 1 attack; or gain 2 hp.
    """
    res = interact.request(zip('gain 1 attack', 'gain 2 hp'))
    if res == 0:
        hero.attack += 1
    elif res == 1:
        states.gain_hp(game, hero, 2)

def hedwig(game, hero):
    default_ally(game, hero)

def invisibility_clock(game, hero):
    # TODO: only to do with harry
    hero.money += 1

def firebolt(game, hero):
    hero.attack += 1
    # TODO: if you defeat a villain.
