"""113"""
def main():
    """SSSS"""
    text = str(input())
    long = len(text)+1
    for _ in range(long):
        text = text.replace('113','')
    print(text)

main()
