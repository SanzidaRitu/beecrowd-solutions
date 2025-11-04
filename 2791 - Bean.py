import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    nums = list(map(int, data[:4]))
    for i, v in enumerate(nums, start=1):
        if v == 1:
            print(i)
            return

    print(-1)

if __name__ == "__main__":
    main()