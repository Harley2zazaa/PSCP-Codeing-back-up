"""Easy Histogram"""
def main():
    """DDD"""
    text = input().replace(' ','')
    word = {}
    for i in text:
        word[i] = word.get(i,0)+1
    sorted_keys = sorted(word.keys(), key=lambda x: (x.lower(), x.isupper()))
    for i in sorted_keys:
        print(f'{i} = {word[i]}')
main()
