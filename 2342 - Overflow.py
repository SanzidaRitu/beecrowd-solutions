N = int(input())
P, Operator, Q = map(str,input().split())
P = int(P)
Q = int(Q)

if (Operator == '+' and P + Q <= N) or (Operator == '*' and P * Q <= N):
    print("OK")
else:
    print("OVERFLOW")