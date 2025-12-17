X = input()
total_digit = len(X)
print(X)

while total_digit > 1:
    X, temp = int(X[:total_digit-1]), int(X[total_digit-1:])
    X = str((X * 3) + temp)
    total_digit = len(X)
    print(X)