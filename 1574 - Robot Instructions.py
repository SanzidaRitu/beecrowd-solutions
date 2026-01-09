t = int(input())

for _ in range(t):
    n = int(input())
    instructions = []
    position = 0

    for _ in range(n):
        command = input().strip()

        if command == "LEFT":
            instructions.append(-1)
        elif command == "RIGHT":
            instructions.append(1)
        else:
            idx = int(command.split()[-1]) - 1
            instructions.append(instructions[idx])

        position += instructions[-1]

    print(position)