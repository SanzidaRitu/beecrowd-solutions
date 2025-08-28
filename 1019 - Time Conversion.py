N = int(input())
hours = N // 3600
N = N % 3600
minutes = N // 60
seconds = N % 60
print(f'{hours}:{minutes}:{seconds}')