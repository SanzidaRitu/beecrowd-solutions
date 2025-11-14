F1, F2 = map(float, input().split())

total_fluctuation = ((1 + F1 / 100) * (1 + F2 / 100) - 1) * 100

print(f"{total_fluctuation:.6f}")