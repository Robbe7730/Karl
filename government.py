from planet import Planet

class Government:
    def __init__(self):
        pass
    
    def handle_turn(state):
        """
        handle_turn: handle the turn, returning the moves
        """

        self.all_planets = state['planets']
        self.my_planets = [p for p in state['planets'] if p['owner'] == 1]
        self.neutral_planets = [p for p in state['planets'] if p['owner'] == None]
        self.enemy_planets = [p for p in state['planets'] if p['owner'] == 2]

        self.all_expeditions = state['expeditions']
        self.my_expeditions = [e for e in state['expeditions'] if e['owner'] == 1]
        self.enemy_expeditions = [e for e in state['expeditions'] if e['owner'] == 2]

        self.my_available_ships = sum([p['ship_count'] for p in self.my_planets])
        self.enemy_available_ships = sum([p['ship_count'] for p in self.enemy_planets])

        self.my_unavailable_ships = sum([p['ship_count'] for p in self.my_expeditions])
        self.enemy_unavailable_ships = sum([p['ship_count'] for p in self.enemy_expeditions])

        self.my_total_ships = self.my_available_ships + self.my_unavailable_ships
        self.enemy_total_ships = self.enemy_available_ships + self.enemy_unavailable_ships
        
        return []
    
    def distress_handler(self):
        pass
