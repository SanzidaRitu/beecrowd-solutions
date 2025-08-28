N = int(input())
ano = N // 365
N = N % 365
mes = N // 30
dia = N % 30
print(str(ano) + ' ano(s)')
print(str(mes) + ' mes(es)')
print(str(dia) + ' dia(s)')