n, I, F = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
count = 0

for i in range(n):
    left = i + 1
    right = n - 1

    while left <= right and arr[i] + arr[left] < I:
        left += 1

    while left <= right and arr[i] + arr[right] > F:
        right -= 1

    if left <= right:
        count += (right - left + 1)

print(count)