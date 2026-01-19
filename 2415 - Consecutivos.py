n = int(input())
numbers = list(map(int, input().split()))

max_count = 1
current_count = 1

for i in range(1, n):
    if numbers[i] == numbers[i - 1]:
        current_count += 1
    else:
        current_count = 1

    if current_count > max_count:
        max_count = current_count

print(max_count)