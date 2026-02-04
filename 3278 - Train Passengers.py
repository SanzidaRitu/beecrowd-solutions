def main():
    C, n = map(int, input().split())
    current = 0

    for i in range(n):
        left, entered, waited = map(int, input().split())

        if left > current:
            print("impossible")
            return
        current -= left

        if current + entered > C:
            print("impossible")
            return
        current += entered

        if waited > 0 and current < C:
            print("impossible")
            return

        if i == n - 1 and waited > 0:
            print("impossible")
            return

    if current != 0:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()