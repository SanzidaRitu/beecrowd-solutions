N = int(input())
A, L, P = map(int, input().split())

if A < N or L < N or P < N:
    print("N")
else:
    print("S")