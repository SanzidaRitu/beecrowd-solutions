t = int(input())

for _ in range(t):
    s = input().strip()

    a = int(s[0])
    b = s[1]
    c = int(s[2])

    if a == c:
        print(a * c)
    elif b.isupper():
        print(c - a)
    else:
        print(a + c)