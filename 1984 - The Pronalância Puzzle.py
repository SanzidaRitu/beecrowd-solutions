N = int(input())
N = str(N)
A = []

for i in N:
    A.append(i)

A.reverse()
print(''.join(A))