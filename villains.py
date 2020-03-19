import states

class Villain:
    def __init__(self, trigger_func, active_state):
        self.func = trigger_func
        self.state = active_state

def quirinus_quirrel_func(game):
    game.active_hero_lose_hp(1)


quirinus_quirrel = Villain(None, states.start_turn)
