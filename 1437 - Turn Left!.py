while True:
    n = int(input())
    if n == 0:
        break

    commands = input().strip()

    directions = ['N', 'L', 'S', 'O']
    current = 0

    for c in commands:
        if c == 'D':
            current = (current + 1) % 4
        elif c == 'E':
            current = (current - 1) % 4

    print(directions[current])