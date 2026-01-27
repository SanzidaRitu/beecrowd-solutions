from itertools import combinations

def can_stack(top, bottom):
    top_faces = [tuple(sorted(face)) for face in combinations(top, 2)]
    bottom_faces = [tuple(sorted(face)) for face in combinations(bottom, 2)]

    for tf in top_faces:
        for bf in bottom_faces:
            if bf[0] > tf[0] and bf[1] > tf[1]:
                return True
    return False

n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    block1 = data[:3]
    block2 = data[3:]

    b1_on_b2 = can_stack(block1, block2)
    b2_on_b1 = can_stack(block2, block1)

    if b1_on_b2 and b2_on_b1:
        print(3)
    elif b1_on_b2:
        print(1)
    elif b2_on_b1:
        print(2)
    else:
        print(0)