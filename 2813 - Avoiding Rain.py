def main():
    N = int(input().strip())
    home = office = 0
    buy_home = buy_office = 0

    for _ in range(N):
        morning, night = input().split()

        if morning == "chuva":
            if home == 0:
                buy_home += 1
                home += 1
            home -= 1
            office += 1

        if night == "chuva":
            if office == 0:
                buy_office += 1
                office += 1
            office -= 1
            home += 1

    print(f"{buy_home} {buy_office}")


if __name__ == "__main__":
    main()