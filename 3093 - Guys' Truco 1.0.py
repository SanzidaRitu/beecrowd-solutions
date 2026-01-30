def main():
    import sys

    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    required = {'Q', 'J', 'K', 'A'}

    for i in range(1, n + 1):
        cards = set(data[i])
        if required.issubset(cards):
            print("Aaah muleke")
        else:
            print("Ooo raca viu")

if __name__ == "__main__":
    main()