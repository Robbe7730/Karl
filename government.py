from planet import Planet

class Government:
    def __init__(self, state):
        self.all_planets = {p['name']:Planet(p,state) for p in state['planets']}
        
    def handle_turn(self, state):
        """
        handle_turn: handle the turn, returning the moves
        """

        
        self.my_planets = {p for p in self.all_planets if p.owner == 1}
        self.neutral_planets = {p for p in self.all_planets if p.owner == None}
        self.enemy_planets = {p for p in self.all_planets if p.owner == 2}

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
        distress_list = []
        for _,p in my_planets:
            distress_list.append([p.name,p.get_distress()])

    
if __name__ == '__main__':
    import json
    f = open("yeetskeet.json", "r")
    state = json.loads(f.readline())
    TestBot = Government(state)
