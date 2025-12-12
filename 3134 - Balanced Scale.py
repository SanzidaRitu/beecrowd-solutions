def solv(a, b, c, d):
    if a + b == c + d \
        or a + c == d + b \
        or a + d == b + c \
        or a == b + c + d \
        or b == c + d + a \
        or c == a + b + d \
        or d == a + b + c:
        return True
    return False

a = int(input().replace('.', ''))
b = int(input().replace('.', ''))
c = int(input().replace('.', ''))
d = int(input().replace('.', ''))

if solv(a, b, c, d):
    print("YES")
else:
    print("NO")