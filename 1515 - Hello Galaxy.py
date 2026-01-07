while True:
    N = int(input())
    if N == 0:
        break

    earliest_year = float('inf')
    earliest_planet = ""

    for _ in range(N):
        name, year, time = input().split()
        year = int(year)
        time = int(time)

        sent_year = year - time

        if sent_year < earliest_year:
            earliest_year = sent_year
            earliest_planet = name

    print(earliest_planet)