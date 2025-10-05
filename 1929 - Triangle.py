s = list(map(int, input().split()))

s.sort()

A = s[0]
B = s[1]
C = s[2]
D = s[3]

def tricond(X,Y,Z):

    if X + Y > Z and X + Z > Y and Z + Y > X:
        ans = True
    else:
        ans = False

    return ans

if tricond(A, B, C) or tricond(A, B, D) or tricond(A, C, D) or tricond(B, C, D):
    print("S")
else:
    print("N")