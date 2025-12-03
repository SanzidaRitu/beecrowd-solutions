score = [float(x) for x in input().split()]
score.sort()
answer = score[1] + score[2] + score[3]
print("%.1f" % answer)