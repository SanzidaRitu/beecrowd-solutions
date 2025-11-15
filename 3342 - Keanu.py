n = int(input().strip())

total = n * n
if total % 2 == 0:
    white = black = total // 2
else:
    white = total // 2 + 1
    black = total // 2

print(f"{white} casas brancas e {black} casas pretas")