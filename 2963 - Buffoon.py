N = int(input())

votes = [int(input()) for _ in range(N)]

max_votes = max(votes)

if votes[0] == max_votes:
    print('S')
else:
    print('N')