def solv(a, b):
    if a >= 6 and b >= 6:
        if (a >= 14 and b >= 14) \
            or (a >= 18 or b >= 18) \
            or (a >= 18 and b >= 14 or b >= 18 and a >= 14):
            return True

    return False

a = int(input())
b = int(input())
print("YES" if solv(a, b) else "NO")