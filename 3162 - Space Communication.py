import math

N = int(input())
ships = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    min_dist = float('inf')
    for j in range(N):
        if i != j:
            dx = ships[i][0] - ships[j][0]
            dy = ships[i][1] - ships[j][1]
            dz = ships[i][2] - ships[j][2]
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            if dist < min_dist:
                min_dist = dist

    if min_dist <= 20:
        print("A")
    elif min_dist <= 50:
        print("M")
    else:
        print("B")