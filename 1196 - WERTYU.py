import sys

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

mapping = {}
for i in range(1, len(keyboard)):
    mapping[keyboard[i]] = keyboard[i - 1]

for line in sys.stdin:
    for ch in line:
        if ch == '\n':
            print()
        elif ch == ' ':
            print(' ', end='')
        else:
            print(mapping[ch], end='')