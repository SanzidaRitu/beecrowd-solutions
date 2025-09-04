n = [int(input())for i in range(100)]
maxval = max(n)
position = n.index(maxval) + 1
print(maxval)
print(position)