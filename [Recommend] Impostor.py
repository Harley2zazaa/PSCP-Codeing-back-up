""""Impostor"""
import json
def main():
    """"SSS"""
    alive = {}
    dead = {}
    while True:
        player = input()
        if player == 'Start':
            break
        playest = json.loads(player)
        alive.update(playest)
    while True:
        action = input()
        if action == 'End':
            break
        die = alive.get(action)
        if die:
            dead.update({action:die})
            alive.pop(action)
    imposter = sum(1 for i in alive.values() if i == 'Impostor')
    alive = dict(sorted(alive.items()))
    dead = dict(sorted(dead.items()))
    print(f"{imposter} Impostor Remains")
    print('***Alive***')
    for i in alive.items():
        print(','.join(i).replace(',', " : "))
    print('***Dead***')
    for j in dead.items():
        print(','.join(j).replace(',', " : "))

main()
