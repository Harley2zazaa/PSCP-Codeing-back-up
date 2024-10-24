"""Music Lover"""
def main():
    """SSS"""
    music = int(input())
    d = {}

    for _ in range(music):
        micle = str(input()).replace('-','ฃ').split('ฃ')
        artist = micle[0]
        musical = micle[1]

        if artist in d:
            d[artist].append(musical)
        else:
            d[artist] = [musical]

    x = d.items()
    for i in x:
        print(i[0])
        for j in i[1]:
            print(j)
main()
