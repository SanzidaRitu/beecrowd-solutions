import math

L = int(input())
c = 0

while L >= 2:
    L /= 2
    c += 1
answer = int(math.pow(4, c))
print(answer)