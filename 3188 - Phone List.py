import sys

def main():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1

    out = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1

        phones = input_data[index:index + n]
        index += n

        phones.sort()

        consistent = True
        for i in range(n - 1):
            if phones[i + 1].startswith(phones[i]):
                consistent = False
                break

        out.append("YES" if consistent else "NO")

    print("\n".join(out))

if __name__ == "__main__":
    main()