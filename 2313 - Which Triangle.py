N = list(map(float, input().split()))

N.sort(reverse=True)

A = N[0]
B = N[1]
C = N[2]

if A + B > C and A + C > B and B + C > A:
    if A != B and B != C and A != C:
        print("Valido-Escaleno")

    elif A == B == C:
        print("Valido-Equilatero")

    elif A == B or B == C or C == A:
        print("Valido-Isoceles")

    if A * A == B * B + C * C:
        print("Retangulo: S")

    else:
        print("Retangulo: N")

else:
    print("Invalido")