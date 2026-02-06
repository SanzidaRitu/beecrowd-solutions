def main():
    N = int(input().strip())

    for _ in range(N):
        name = input().strip()
        scores = list(map(float, input().split()))

        if len(scores) == 1:
            scores.append(0.0)

        if len(scores) == 4:
            scores.remove(min(scores))

        average = sum(scores) / len(scores)
        print(f"{name}: {average:.1f}")

if __name__ == "__main__":
    main()