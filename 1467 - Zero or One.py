import sys

for line in sys.stdin:
    A, B, C = map(int, line.split())

    if A == B == C:
        print("*")
    elif A != B and A != C:
        print("A")
    elif B != A and B != C:
        print("B")
    else:
        print("C")