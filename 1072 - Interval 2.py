N = int(input())
inside = 0
out = 0

for i in range(N):
    x = int(input())
    if 10 <= x <= 20:
        inside += 1
    else:
        out += 1

print(f'{inside} in')
print(f'{out} out')