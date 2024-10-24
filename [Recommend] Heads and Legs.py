"""Heads and Legs"""
def main():
    """SSS"""
    animal = int(input())
    leg = int(input()) #2x+4y = leg ?

    if leg % 2:
        print('Impossible')
        return

    rabbits = (leg // 2) - animal
    birb = animal - rabbits

    if rabbits < 0 or birb < 0:
        print('Impossible')
        return
    print(rabbits,end=' ')
    print(birb)

main()
