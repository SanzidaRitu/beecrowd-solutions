def to_ms(t):
    m, s, ms = map(int, t.split(':'))
    return m * 60000 + s * 1000 + ms

def main():
    N, V = map(int, input().split())

    drivers = []

    for _ in range(N):
        data = input().split()
        pid = int(data[0])
        laps = list(map(to_ms, data[1:]))

        total = 0
        cumulative = []
        for lap in laps:
            total += lap
            cumulative.append(total)

        drivers.append({
            "id": pid,
            "laps": laps,
            "cum": cumulative,
            "total": total
        })

    best = None

    for d in drivers:
        for i, lap in enumerate(d["laps"]):
            candidate = (lap, i, d["cum"][i], d["id"])
            if best is None or candidate < best:
                best = candidate

    best_driver_id = best[3]

    drivers.sort(key=lambda d: d["total"])

    top10_ids = {drivers[i]["id"] for i in range(min(10, N))}

    if best_driver_id in top10_ids:
        print(best_driver_id)
    else:
        print("NENHUM")

if __name__ == "__main__":
    main()