def alohomora(game):
    ''' Spell
    Gain 1 influence.
    '''
    game.active_hero().influence += 1

def firebolt(game):
    ''' Item
    Gain 1 attack.
    If you defeat a Villain, also gain 1 influence.
    '''
    game.active_hero().attack += 1
    # TODO

def default_ally(game):
    ''' Ally
    Choose one:
    Gain 1 attack; or gain 2 health.
    '''
    # TODO: choose 1???