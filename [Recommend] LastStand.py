"""SANSSSSS"""
def main():
    """dwdwdwd"""
    text = str(input()).replace('[','').replace(']','').split(',')
    last = []
    for i in text:
        last_num = int(i)%10
        last.append(last_num)
    for j in last:
        print(j)
main()
