N, S = map(int, input().split())

saldo = S
menor = S

for _ in range(N):
    variacao = int(input())
    saldo += variacao
    if saldo < menor:
        menor = saldo

print(menor)