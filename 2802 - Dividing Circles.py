import sys


def main():
    data = sys.stdin.read().strip().split()

    if not data:
        return
    n = int(data[0])

    c2 = n * (n - 1) // 2

    if n >= 4:
        c4 = n * (n - 1) * (n - 2) * (n - 3) // 24

    else:
        c4 = 0
    result = 1 + c2 + c4

    print(result)

if __name__ == "__main__":
    main()