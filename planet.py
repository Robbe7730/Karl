"""
planet: contains the Planet class
"""

class Planet:
    """
    Planet: represents an owned planet
    """
    def __init__(self, pw_planet):
        self.owner = pw_planet["owner"]
        self.x = pw_planet["x"]
        self.y = pw_planet["y"]
        self.ship_count = pw_planet["ship_count"]
        self.name = pw_planet["name"]

        self._handles_distress = False
        self._handles_attacks = False
        self._target = None
        self._moves = []
        
    def handle_turn(self, _state):
        """
        handle_turn: process the new turn
        """

    def get_moves(self) -> list:
        """
        get_moves: return the moves this planet intends to take
        """

    def get_future(self):
        """
        get_future: getter for the future states of this planet
        """
        return iter(lambda _: (1,0), 1)

    def get_distress(self) -> list[tuple[int, int]]:
        """
        get_distress: returns the times this planet will go into distress and
        the amount of ships it needs to survive
        """

    def set_target_ship_count(self, num_ships: int, increment: int):
        """
        set_target_ship_count: set the target number of ships for this planet to
        num_ships, increasing by increment every turn
        """

    # ===== DISTRESS CALLS =====

    def query_distress_call(self, call_handles: list) -> (bool, list):
        """
        query_distress_call: ask the planet how it can handle the distress calls
        returning (has_changed, new_call_handles)
        """

    def execute_distress_call(self, call_handles: list):
        """
        execute_distress_call: execute all distress call handling
        """

    # ===== ATTACK CALLS =====

    def query_attack_call(self, call_handles: list) -> (bool, list):
        """
        query_attack_call: ask the planet how it can handle the attack calls
        returning (has_changed, new_call_handles)
        """

    def execute_attack_call(self, call_handles: list):
        """
        execute_attack_call: execute all attack call handling
        """

    # ===== OBJECTIVE CHANGES =====

    def make_feeder(self, other_planet):
        """
        make_feeder: make the planet a feeder planet to other_planet, keeping
        only ships_to_keep ships
        """
        self._target = other_planet
        self._handles_distress = True
        self._handles_attacks = False

    def make_defender(self):
        """
        make_defender: make the planet a defender planet
        - hoard ships
        - handle distress calls
        """
        self._target = None
        self._handles_distress = True
        self._handles_attacks = False

    def make_attacker(self, other_planet):
        """
        make_attacker: make the planet a attacker planet
        """
        self._target = other_planet
        self._handles_distress = True
        self._handles_attacks = True

    def make_idle(self):
        """
        make_idle: make the planet an idle planet
        """
        self._target = None
        self._handles_distress = False
        self._handles_attacks = False
