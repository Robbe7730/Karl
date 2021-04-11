from planet import Planet

class Government:
    def __init__(self, state):
        self.all_planets = {p['name']:Planet(p,state) for p in state['planets']}
        
    def handle_turn(self, state):
        """
        handle_turn: handle the turn, returning the moves
        """

        
        self.my_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == 1}
        self.neutral_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == None}
        self.enemy_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == 2}

        self.all_expeditions = state['expeditions']
        self.my_expeditions = [e for e in state['expeditions'] if e['owner'] == 1]
        self.enemy_expeditions = [e for e in state['expeditions'] if e['owner'] == 2]

        self.my_available_ships = sum([p.ship_count for (k,p) in self.my_planets.items()])
        self.enemy_available_ships = sum([p.ship_count for (k,p) in self.enemy_planets.items()])

        self.my_unavailable_ships = sum([p['ship_count'] for p in self.my_expeditions])
        self.enemy_unavailable_ships = sum([p['ship_count'] for p in self.enemy_expeditions])

        self.my_total_ships = self.my_available_ships + self.my_unavailable_ships
        self.enemy_total_ships = self.enemy_available_ships + self.enemy_unavailable_ships
        
        return []
    
    def distress_handler(self):
        distress_list = []
        for p in self.my_planets.values():
            for request in p.get_distress():
                distress_list.append([p.name,request,None])
        my_planets = list(self.my_planets.values())
        i = 0
        lastchanged = 1
        notoptimal = True
        while notoptimal:
            changed, distress_list = my_planets[i].query_distress_call(distress_list)
            if lastchanged == i:
                notoptimal = False
            if changed:
                lastchanged = i
            i = (i+1)%len(my_planets)
        execute_distress_call(distress_list)


if __name__ == '__main__':
    import json
    f = open("yeetskeet.json", "r")
    state = json.loads(f.readline())
    TestBot = Government(state)
    TestBot.handle_turn(state)
    TestBot.distress_handler()
