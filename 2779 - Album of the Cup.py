N = int(input())
M = int(input())

purchased = []

for i in range(M):
    z = int(input())
    purchased.append(z)

already_purchased = set(purchased)
missing_qnt = len(already_purchased)

answer = N - missing_qnt
print(answer)