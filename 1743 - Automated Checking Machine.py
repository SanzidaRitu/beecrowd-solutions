def solve():
    plug = list(map(int, input().split()))
    socket = list(map(int, input().split()))

    for i in range(5):
        if plug[i] == socket[i]:
            print("N")
            return

    print("Y")

if __name__ == "__main__":
    solve()