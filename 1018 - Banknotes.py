N = int(input())
print(N)

print(str(N // 100) + ' nota(s) de R$ 100,00')
N = N % 100

print(str(N // 50) + ' nota(s) de R$ 50,00')
N = N % 50

print(str(N // 20) + ' nota(s) de R$ 20,00')
N = N % 20

print(str(N // 10) + ' nota(s) de R$ 10,00')
N = N % 10

print(str(N // 5) + ' nota(s) de R$ 5,00')
N = N % 5

print(str(N // 2) + ' nota(s) de R$ 2,00')
N = N % 2

print(str(N // 1) + ' nota(s) de R$ 1,00')