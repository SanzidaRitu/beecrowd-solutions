import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    H = list(map(int, input().split()))

    arrows = {}
    answer = 0

    for h in H:
        if arrows.get(h, 0) > 0:
            arrows[h] -= 1
        else:
            answer += 1

        arrows[h - 1] = arrows.get(h - 1, 0) + 1

    print(answer)

solve()