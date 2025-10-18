n = int(input())
k = int(input())

competitor = [int(input()) for x in range(n)]
competitor.sort(reverse = True)
total = k

while total < n and competitor[total] == competitor[k - 1]:
    total += 1

print(total)