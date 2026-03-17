J, R = map(int, input().split())
points = list(map(int, input().split()))

scores = [0] * J

for i in range(J * R):
    player = i % J
    scores[player] += points[i]

max_score = max(scores)

for i in range(J * R - 1, -1, -1):
    player = i % J
    if scores[player] == max_score:
        print(player + 1)
        break