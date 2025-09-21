n = int(input())

id = list(map(int, input().split()))

minval = min(id)
minindex = id.index(minval) + 1

print(minindex)