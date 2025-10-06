P, N =  map(int,input().split())

PN = list(map(int,input().split()))
output = 0

for i in range(len(PN) - 1):
    if abs(PN[i]-PN[i + 1]) > P:
        output = 1
        break
    else:
        output = 0

if output == 1:
    print("GAME OVER")
else:
    print("YOU WIN")