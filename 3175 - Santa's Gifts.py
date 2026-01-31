def main():
    N = int(input())
    g = list(map(int, input().split()))

    children = [(g[i], i) for i in range(N)]

    children.sort()

    gifts = [0] * N
    current_gift = 1

    for i, (good_deeds, idx) in enumerate(children):
        if i == 0:
            gifts[idx] = 1
        else:
            prev_good, prev_idx = children[i - 1]
            if good_deeds == prev_good:
                gifts[idx] = gifts[prev_idx]
            else:
                gifts[idx] = gifts[prev_idx] + 1

    print(sum(gifts))

if __name__ == "__main__":
    main()