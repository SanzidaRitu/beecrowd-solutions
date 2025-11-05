def position_to_coords(pos):
    column = ord(pos[0]) - ord('a') + 1
    row = int(pos[1])
    return column, row

p1, p2 = input().split()

x1, y1 = position_to_coords(p1)
x2, y2 = position_to_coords(p2)

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("VALIDO")

else:
    print("INVALIDO")