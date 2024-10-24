"""PickThemAgain"""
def main():
    """SSSS"""
    number = str(input()).split(' ')
    number_three_five = []
    for i in number[::-1]:
        if not int(i)%3 or not int(i)%5 :
            number_three_five.append(i)
    if number_three_five:
        for j in number_three_five:
            print(j)
    else:
        print('Nope')
main()
