import sys

input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1

for case in range(1, T + 1):
    N = int(data[index])
    index += 1

    grades = list(map(int, data[index:index + N]))
    index += N

    max_value = max(grades)

    longest = 0
    current = 0

    for grade in grades:
        if grade == max_value:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print(f"Caso #{case}: {longest}")