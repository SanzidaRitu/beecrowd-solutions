def solve(A, B):
    XOR = A ^ B
    count = 0

    while (XOR):
        XOR = XOR & (XOR - 1)
        count += 1
    return count


while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break

    distance = solve(x, y)
    print(distance)