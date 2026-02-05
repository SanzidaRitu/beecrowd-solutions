def main():
    N = int(input().strip())
    s = input().strip()

    ans = 0
    i = 0

    while i < N:
        j = i
        while j < N and s[j] == s[i]:
            j += 1

        length = j - i

        if s[i] == 'a' and length >= 2:
            ans += length

        i = j

    print(ans)

if __name__ == "__main__":
    main()