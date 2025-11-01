jewels = set()

try:
    while True:
        jewel = input().strip()

        if jewel:
            jewels.add(jewel)

except EOFError:
    pass

print(len(jewels))