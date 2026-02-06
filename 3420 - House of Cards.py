def cards_needed(N):
    return (3 * N * N + N) // 2

def main():
    T = int(input().strip())

    for _ in range(T):
        C = int(input().strip())

        low, high = 1, 10 ** 9
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if cards_needed(mid) <= C:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        print(ans)

if __name__ == "__main__":
    main()