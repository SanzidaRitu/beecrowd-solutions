N = int(input())
idl = []
scorelist = []

for i in range(N):

    ids, score = map(float, input().split())
    idl.append(ids)
    scorelist.append(score)

maxscore = max(scorelist)
if maxscore >= 8:
    maxscoreindex = scorelist.index(maxscore)
    print(int(idl[maxscoreindex]))
else:
    print("Minimum note not reached")