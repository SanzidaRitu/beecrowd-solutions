Am, Rm, Em = map(int, input().split())
Av, Rv, Ev = map(int, input().split())

S = input()
n = len(S)

time_m = 2 * Am + Rm + Em * n
time_v = 2 * Av + Rv + Ev * n

if time_m < time_v:
    print("Matheus")
elif time_v < time_m:
    print("Vinicius")
else:
    print("Empate")