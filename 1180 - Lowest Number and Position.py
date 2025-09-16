N = int(input())
X = list(map(int, input().split()))

minval = min(X)
minpos = X.index(minval)

print(f"Menor valor: {minval}")
print(f"Posicao: {minpos}")