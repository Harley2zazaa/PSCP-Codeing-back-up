"""SS"""
def main():
    """SSSS"""
    number = input()
    answer = 0
    for i in range(len(number) - 1):
        if int(number[i]) + int(number[i + 1]) == 10:
            answer += 1
    for j in range(len(number) - 2):
        if int(number[j]) + int(number[j + 1]) + int(number[j + 2]) == 10:
            answer += 1
    for z in range(len(number) - 3):
        if int(number[z]) + int(number[z + 1]) + int(number[z + 2]) + int(number[z + 3]) == 10:
            answer += 1
    for s in range(len(number) - 4):
        if int(number[s]) + int(number[s + 1]) + int(number[s + 2]) + int(number[s + 3])\
        + int(number[s + 4])== 10:
            answer += 1
    for d in range(len(number) - 5):
        if int(number[d]) + int(number[d + 1]) + int(number[d + 2]) + int(number[d + 3])\
        + int(number[d + 4])+ int(number[d + 5])== 10:
            answer += 1
    print(answer)

main()
