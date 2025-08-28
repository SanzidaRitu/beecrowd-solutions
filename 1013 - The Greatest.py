A, B, C = map(int, input().split())
MaiorAB = (((A + B + abs(A - B)) // 2) + C + abs(((A + B + abs(A - B)) // 2) - C)) // 2
print(str(MaiorAB) + ' eh o maior')