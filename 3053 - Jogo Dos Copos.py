N = int(input())
moeda = input().strip()

movimentos = {
    1: ('A', 'B'),
    2: ('B', 'C'),
    3: ('A', 'C')
}

for _ in range(N):
    tipo = int(input())
    a, b = movimentos[tipo]

    if moeda == a:
        moeda = b
    elif moeda == b:
        moeda = a

print(moeda)