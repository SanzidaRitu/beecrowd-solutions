while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    alice = set(map(int, input().split()))
    beatriz = set(map(int, input().split()))

    alice_unique = alice - beatriz
    beatriz_unique = beatriz - alice

    print(min(len(alice_unique), len(beatriz_unique)))