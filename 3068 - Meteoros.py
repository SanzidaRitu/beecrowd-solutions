def main():
    test_case = 1
    while True:
        X1, Y1, X2, Y2 = map(int, input().split())
        if X1 == Y1 == X2 == Y2 == 0:
            break

        N = int(input())
        count = 0
        for _ in range(N):
            x, y = map(int, input().split())
            if X1 <= x <= X2 and Y2 <= y <= Y1:
                count += 1

        print(f"Teste {test_case}")
        print(count)

        test_case += 1

if __name__ == "__main__":
    main()