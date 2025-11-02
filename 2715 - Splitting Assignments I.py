while True:
    try:
        n = int(input())
        numbers = list(map(int, input().split()))

        total = sum(numbers)
        left_sum = 0
        min_diff = float('inf')

        for i in range(n - 1):
            left_sum += numbers[i]
            right_sum = total - left_sum
            diff = abs(left_sum - right_sum)
            min_diff = min(min_diff, diff)

        print(min_diff)

    except EOFError:
        break