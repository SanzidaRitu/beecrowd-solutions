numbers = list(map(int, input().split()))

max_value = 0

for num in numbers:
    if num == 0:
        break
    if num > max_value:
        max_value = num

print(max_value)