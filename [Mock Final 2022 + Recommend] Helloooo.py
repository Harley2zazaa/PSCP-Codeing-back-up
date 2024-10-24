""""Helloooo"""
def main():
    """SS"""
    text = str(input())
    sara = 'aeoui'
    pol = -1
    for i in sara:
        index = text.rfind(i)
        if index > pol:
            pol = index
    if pol != -1:
        print(text[:pol]+text[pol]*4+text[pol+1:])
    else:
        print(text)
main()
