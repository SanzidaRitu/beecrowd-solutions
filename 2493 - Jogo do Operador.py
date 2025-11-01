import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    T = int(line)
    exprs = []

    for _ in range(T):
        part = sys.stdin.readline().strip()
        x_str, yz = part.split()
        y_str, z_str = yz.split('=')
        X = int(x_str)
        Y = int(y_str)
        Z = int(z_str)
        exprs.append((X, Y, Z))

    wrong = []

    for _ in range(T):
        part = sys.stdin.readline().strip().split()
        name = part[0]
        E = int(part[1]) - 1
        R = part[2]
        X, Y, Z = exprs[E]
        correct = False

        if R == '+':
            correct = (X + Y == Z)

        elif R == '-':
            correct = (X - Y == Z)

        elif R == '*':
            correct = (X * Y == Z)

        elif R == 'I':
            if (X + Y != Z) and (X - Y != Z) and (X * Y != Z):
                correct = True

        if not correct:
            wrong.append(name)

    if len(wrong) == 0:
        print("You Shall All Pass!")

    elif len(wrong) == T:
        print("None Shall Pass!")

    else:
        wrong.sort()
        print(" ".join(wrong))