import sys, json, random

from government import Government

def move(moves):
    record = { 'moves': moves }
    print(json.dumps(record))
    sys.stdout.flush()

state = json.loads(next(sys.stdin))

government = Government(state)

for line in sys.stdin:
    move(government.handle_turn(state))
    state = json.loads(line)

move(government.handle_turn(state))
