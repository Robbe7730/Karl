import sys, json, random

from government import Government

def move(moves):
    record = { 'moves': moves }
    print(json.dumps(record))
    sys.stdout.flush()

government = Government()

for line in sys.stdin:
    state = json.loads(line)
    move(government.handle_turn(state))
