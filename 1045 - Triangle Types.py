A, B, C = sorted(map(float, input().split()), reverse=True)

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A * A == B * B + C * C:
        print('TRIANGULO RETANGULO')
    elif A * A > B * B + C * C:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')