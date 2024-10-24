"""SSSS"""
TEXT = str(input()).split()
MEMO = []
ALREADY = ""

for WORD in TEXT:
    if WORD != ALREADY:
        MEMO.append(WORD)
        ALREADY = WORD

print(" ".join(MEMO))
