def count_overtakes(start, finish):
    position = {car: i for i, car in enumerate(finish)}

    indexed_start = [position[car] for car in start]

    overtakes = 0

    for i in range(len(indexed_start)):
        for j in range(i + 1, len(indexed_start)):
            if indexed_start[i] > indexed_start[j]:
                overtakes += 1

    return overtakes


while True:
    try:
        n = int(input())
        start = list(map(int, input().split()))
        finish = list(map(int, input().split()))

        print(count_overtakes(start, finish))
    except EOFError:
        break