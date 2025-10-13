N = int(input())

S = 0
B = 0
A = 0

S1 = 0
B1 = 0
A1 = 0

for i in range(N):
    name = input()
    S_i, B_i, A_i = map(int, input().split())
    S_i_s, B_i_s, A_i_s = map(int, input().split())

    S += S_i
    S1 += S_i_s
    B += B_i
    B1 += B_i_s
    A += A_i
    A1 += A_i_s

S_p = (S1 / S) * 100
B_p = (B1 / B) * 100
A_p = (A1 / A) * 100

print(f"Pontos de Saque: {S_p:.2f} %.")
print(f"Pontos de Bloqueio: {B_p:.2f} %.")
print(f"Pontos de Ataque: {A_p:.2f} %.")