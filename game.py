import states

class Game:
    def __init__(self, num_players: int, locations: list):
        """
        Initialize the game.

        Arguments:
        - num_players: Number of players in this game.
        - locations: An array of counts of controls in the locations.
        """
        self.num_players = num_players
        self.locations = locations
        self.this_location_max = self.locations.pop()
        self.this_location_remain = self.this_location_max
        self.active_hero = None

    def reveal_dark_arts(self):
        """
        Reveals a dark arts card.
        """
        # TODO
        pass

    def location_info(self):
        """
        Returns the current location infomation.

        Returns:
        (remain, max) of this location.
        """
        return self.this_location_remain, self.this_location_max

    def update_state(self, state, args):
        # TODO: Implement state update
        # This will be a big function
        """
        Responds to the given state. Notice that the state passed in may
        trigger other states.

        Arguments:
        - state: the state to respond. It should be a function in states.py
        """
        state(self, *args)

