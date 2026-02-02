def solve():
    N = int(input().strip())
    A = input().strip()
    B = input().strip()

    if N % 2 == 0:
        print("Deletion succeeded" if A == B else "Deletion failed")
    else:
        flipped = ''.join('1' if c == '0' else '0' for c in A)
        print("Deletion succeeded" if flipped == B else "Deletion failed")

if __name__ == "__main__":
    solve()