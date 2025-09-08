nums = list(map(int, input().split()))

a = nums[0]
n = 0
for value in nums[1:]:
    if value > 0:
        n = value
        break

s = 0
for i in range(n):
    s += a + i

print(s)