if __name__ == "__main__":
    t = 0

    while True:
        n = int(input())
        if n == 0:
            break

        t += 1
        print('Teste', t)
        remain = 0

        for i in range(n):
            j, z = map(int, input().split())
            remain += (j - z)
            print(remain)
        print()