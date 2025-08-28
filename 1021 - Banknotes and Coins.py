N = float(input())
print('NOTAS:')

print(str(int(N // 100)) + ' nota(s) de R$ 100.00')
N = N % 100

print(str(int(N // 50)) + ' nota(s) de R$ 50.00')
N = N % 50

print(str(int(N // 20)) + ' nota(s) de R$ 20.00')
N = N % 20

print(str(int(N // 10)) + ' nota(s) de R$ 10.00')
N = N % 10

print(str(int(N // 5)) + ' nota(s) de R$ 5.00')
N = N % 5

print(str(int(N // 2)) + ' nota(s) de R$ 2.00')
N = N % 2

print('MOEDAS:')
N = N * 100

print(str(int(N // 100)) + ' moeda(s) de R$ 1.00')
N = N % 100

print(str(int(N // 50)) + ' moeda(s) de R$ 0.50')
N = N % 50

print(str(int(N // 25)) + ' moeda(s) de R$ 0.25')
N = N % 25

print(str(int(N // 10)) + ' moeda(s) de R$ 0.10')
N = N % 10

print(str(int(N // 5)) + ' moeda(s) de R$ 0.05')
N = N % 5

print(str(int(N // 1)) + ' moeda(s) de R$ 0.01')