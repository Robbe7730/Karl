"""
planet: contains the Planet class
"""

class Planet:
    """
    Planet: represents an owned planet
    """
    def handle_turn(self, _state):
        """
        handle_turn: process the new turn
        """

    def get_moves(self) -> list:
        """
        get_moves: return the moves this planet intends to take
        """

    def get_distress(self) -> list[tuple[int, int]]:
        """
        get_distress: returns the times this planet will go into distress and
        the amount of ships it needs to survive
        """
    
    def get_future(self):
        """
        get_future: getter for the future states of this planet
        """
        return iter(lambda _: (1,0), 1)

    def set_target_ship_count(self, num_ships: int, increment: int):
        """
        set_target_ship_count: set the target number of ships for this planet to
        num_ships, increasing by increment every turn
        """

    def query_distress_call(self, call_handles: list) -> (bool, list):
        """
        query_distress_call: ask the planet how it can handle the distress calls
        returning (has_changed, new_call_handles)
        """

    def execute_distress_call(self, call_handles: list) -> (bool, list):
        """
        execute_distress_call: execute all distress call handling
        """

    def query_attack_call(self, call_handles: list) -> (bool, list):
        """
        query_attack_call: ask the planet how it can handle the attack calls
        returning (has_changed, new_call_handles)
        """

    def execute_attack_call(self, call_handles: list) -> (bool, list):
        """
        execute_attack_call: execute all attack call handling
        """

    def make_feeder(self, other_planet: Planet):
        """
        make_feeder: make the planet a feeder planet to other_planet, keeping
        only ships_to_keep ships
        """

    def make_defender(self):
        """
        make_defender: make the planet a defender planet
        - hoard ships
        - handle distress calls
        """

    def make_attacker(self, other_planet: Planet):
        """
        make_attacker: make the planet a attacker planet
        """

    def make_idle(self):
        """
        make_idle: make the planet an idle planet
        """
