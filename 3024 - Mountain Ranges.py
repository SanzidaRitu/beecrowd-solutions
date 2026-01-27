N, X = map(int, input().split())
A = list(map(int, input().split()))

max_viewpoints = 1
current_count = 1

for i in range(1, N):
    if A[i] - A[i - 1] <= X:
        current_count += 1
    else:
        current_count = 1

    if current_count > max_viewpoints:
        max_viewpoints = current_count

print(max_viewpoints)