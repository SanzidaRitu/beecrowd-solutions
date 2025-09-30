import math

while True:
    line = input().split()
    if line[0] == '0':
        break

    A = int(line[0])
    B = int(line[1])
    C = int(line[2])

    rectangular = A * B

    house = (rectangular * 100) / C

    side = math.sqrt(house)

    print(int(side))
