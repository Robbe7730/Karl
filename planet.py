"""
planet: contains the Planet class
"""


class FutureIterator:
    """
    FutureIterator: iterator for the future of a planet
    """

    def __init__(self, ship_count, incoming_expeditions, use_distress, owner=1):
        self.ship_count = ship_count
        self.use_distress = use_distress
        self.owner = owner

        self.turn = 1
        self.incoming_expeditions = incoming_expeditions
        self.incoming_expeditions.sort(
            key=lambda x: x["turns_remaining"],
            reverse=True
        )

    def __iter__(self):
        return self

    def __next__(self):
        self.ship_count += 1

        contestants = {}

        contestants[self.owner] = self.ship_count

        while (len(self.incoming_expeditions) > 0 and
                self.turn >= self.incoming_expeditions[-1]["turns_remaining"]):

            incoming = self.incoming_expeditions.pop()

            if incoming["owner"] not in contestants:
                contestants[incoming["owner"]] = 0

            contestants[incoming["owner"]] += incoming["ship_count"]

        if len(contestants) > 1:
            contestants_sorted = sorted(
                contestants.items(),
                key=lambda x: -x[1]
            )

            new_owner, attacking_ships = contestants_sorted[0]
            _, defending_ships = contestants_sorted[1]

            new_ship_count = attacking_ships - defending_ships
        else:
            new_owner, new_ship_count = next(iter(contestants.items()))

        if new_ship_count == 0:
            new_owner = 0

        if self.use_distress and new_owner != 1:
            new_owner = 1
            new_ship_count = 1

        self.ship_count = new_ship_count
        self.owner = new_owner

        self.turn += 1

        return self.ship_count if self.owner == 1 else -self.ship_count


class Planet:
    """
    Planet: represents an owned planet
    """

    def __init__(self, pw_planet, state):
        self.owner = pw_planet["owner"]
        self.x = pw_planet["x"]
        self.y = pw_planet["y"]
        self.ship_count = pw_planet["ship_count"]
        self.name = pw_planet["name"]

        self._handles_distress = False
        self._handles_attacks = False
        self._target = None
        self._moves = []
        self._distance_to_furthest = max(
            self.distance_to(x) for x in state["planets"]
        )
        self._inbound_expeditions = []

    def handle_turn(self, state):
        """
        handle_turn: process the new turn
        """
        self._inbound_expeditions = [
            x for x in state["expeditions"] if x["owner"] == 1
        ]

    def get_moves(self) -> list:
        """
        get_moves: return the moves this planet intends to take
        """

    def get_future(self, assume_distress=False):
        """
        get_future: getter for the future states of this planet
        """
        return FutureIterator(
            self.ship_count,
            self._inbound_expeditions,
            assume_distress,
            self.owner
        )

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
        if not self._handles_distress:
            return (False, call_handles)

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
        if not self._handles_attacks:
            return (False, call_handles)

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

    def make_attacker(self):
        """
        make_attacker: make the planet a attacker planet
        """
        self._handles_distress = True
        self._handles_attacks = True

    def make_idle(self):
        """
        make_idle: make the planet an idle planet
        """
        self._target = None
        self._handles_distress = False
        self._handles_attacks = False

    # ===== HELPER FUNCTIONS =====

    def distance_to(self, p2):
        dx = self.x - p2["x"]
        dy = self.y - p2["y"]

        return (dx * dx + dy * dy) ** 0.5
