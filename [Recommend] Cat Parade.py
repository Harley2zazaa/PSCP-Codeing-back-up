""" asd """
def main():
    """ asd """
    cats = []
    x = []
    while True:
        word = input()
        if word == "END":
            break
        if word != "IT'S A DOG":
            for cat in word.split(","):
                cat = cat.strip()
                cats.append(cat)
                if not cat in x:
                    x.append(cat)
        else:
            if cats:
                cats.pop()
            if x:
                x.pop()
    x.sort()
    for cat in x:
        print(cat, cats.index(cat) + 1, cats.count(cat))
main()
