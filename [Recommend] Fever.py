"""Fever"""
def main():
    """DDDD"""
    cel = float(input())
    if cel < 38:
        print('No Fever')
    elif 38 <= cel < 39:
        print('Mild Fever')
    elif 39 <= cel < 40:
        print('High Fever')
    else:
        print('Very High Fever')
main()
