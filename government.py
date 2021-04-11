from planet import Planet

class Government:
    def __init__(self, state):
        self.all_planets = {p['name']:Planet(p,state) for p in state['planets']}
        
        
    def handle_turn(self, state):
        """
        handle_turn: handle the turn, returning the moves
        """
        for p in self.all_planets.values():
            p.handle_turn(state)

        self.update_parameters(state)
        self.distress_handler()
        self.production_handler()





        output = []
        for p in self.all_planets.values():
            output.append(p.get_moves())
        return output
    

    def update_parameters(self,state):
        self.my_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == 1}
        self.neutral_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == None}
        self.enemy_planets = {k:p for (k,p) in self.all_planets.items() if p.owner == 2}

        self.all_expeditions = state['expeditions']
        self.my_expeditions = [e for e in state['expeditions'] if e['owner'] == 1]
        self.enemy_expeditions = [e for e in state['expeditions'] if e['owner'] == 2]

        self.my_available_ships = sum([p.ship_count for (k,p) in self.my_planets.items()])
        self.neutral_ships = sum([p.ship_count for (k,p) in self.neutral_planets.items()])
        self.enemy_available_ships = sum([p.ship_count for (k,p) in self.enemy_planets.items()])

        self.my_unavailable_ships = sum([p['ship_count'] for p in self.my_expeditions])
        self.enemy_unavailable_ships = sum([p['ship_count'] for p in self.enemy_expeditions])

        self.my_total_ships = self.my_available_ships + self.my_unavailable_ships
        self.enemy_total_ships = self.enemy_available_ships + self.enemy_unavailable_ships
        
    
    def distress_handler(self):
        distress_list = []
        for p in self.my_planets.values():
            for (ship_request,request_before) in p.get_distress():
                distress_list.append([p.name,ship_request,request_before,None])
        
        my_planets = list(self.my_planets.values())
        i = 0
        lastchanged = -1
        notoptimal = True
        while notoptimal:
            changed, distress_list = my_planets[i].query_distress_call(distress_list)
            if lastchanged == i:
                notoptimal = False
            if changed:
                lastchanged = i
            i = (i+1)%len(my_planets)
        execute_distress_call(distress_list)
        

    def production_handler(self):
        ship_difference = self.my_total_ships - self.enemy_total_ships
        production_difference = len(self.my_planets) - len(self.enemy_planets)

        
        if ship_difference >= 0 and production_difference >= 0:
            print('Winning/Neutral')
            # Take more planets
        elif ship_difference >= 0 and production_difference < 0:
            print('Losing in ' + -ship_difference/production_difference + ' turns')
            # Take more planets
        elif ship_difference <= 0 and production_difference > 0:
            print('Winning in ' + -ship_difference/production_difference + ' turns')
            # Wait a little taking planets
        elif ship_difference <= 0 and production_difference <= 0:
            print('Losing/Neutral')
            # Take whatever, were losing anyway


        average_neutral_ships = self.neutral_ships/len(self.neutral_planets)

    def frontline_handler(self)
        # Determine frontline
        
        # Interpolate surface over enemy planets shipcount (area weighted)
        # Project shipcount surface to frontline for ship target determination
        
        # Interpolate surface over enemy planets planetdensity
        # Project planetdensity surface to frontline for increment determination
        



if __name__ == '__main__':
    import json
    f = open("yeetskeet.json", "r")
    state = json.loads(f.readline())
    TestBot = Government(state)
    TestBot.handle_turn(state)
    TestBot.distress_handler()
