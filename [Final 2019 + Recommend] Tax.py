"""Tax"""
def main():
    """SSS"""
    year = int(input())
    motor = int(input())
    discount = 0
    cost = 0
    if motor <= 600:
        cost = stepi(motor)
    if 601 <= motor <= 1800:
        cost = stepii(motor-600)+300
    if motor > 1800:
        cost = stepiii(motor-1800)+2100
    if year == 6:
        discount = cost*(0.1)
    if year == 7:
        discount = cost*(0.2)
    if year == 8:
        discount = cost*(0.3)
    if year == 9:
        discount = cost*(0.4)
    if year >= 10:
        discount = cost*(0.5)
    print(f'{(cost-discount):.2f}')
def stepi(motor):
    """SSS"""
    return motor*(0.5)
def stepii(moter):
    """SSS"""
    return moter*1.50
def stepiii(moter):
    """SSS"""
    return moter*4
main()
