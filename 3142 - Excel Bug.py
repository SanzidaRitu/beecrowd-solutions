import sys

def column_to_number(col):
    num = 0
    for c in col:
        num = num * 26 + (ord(c) - ord('A') + 1)
    return num

MAX_COLUMN = column_to_number("XFD")

for line in sys.stdin:
    col = line.strip()
    if not col:
        continue

    num = column_to_number(col)
    if 1 <= num <= MAX_COLUMN:
        print(num)
    else:
        print("Essa coluna nao existe Tobias!")