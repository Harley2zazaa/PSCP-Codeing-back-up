"""Diamond I"""
def main():
    """S"S"""
    deep = int(input())
    leagh = int(input())
    layer = []
    for _ in range(deep):
        floor = input().split(' ')
        layer.extend([floor])
    base = -float('inf')
    position = 0
    while position < leagh:
        point = 0
        for i in range(0,deep):
            point += int(layer[i][position])
        position += 1
        if base <= point:
            base = point
    print(base)
main()
