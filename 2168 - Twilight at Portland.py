quad = int(input())
camera = [input().split() for x in range(quad+1)]

for x in range(quad):
    for y in range(quad):
        if int(camera[x][y]) + int(camera[x][y + 1]) + int(camera[x + 1][y]) + int(camera[x + 1][y + 1]) < 2:
            print("U", end="")

        else:
            print("S", end="")
    print()