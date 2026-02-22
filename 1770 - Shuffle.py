import sys

for line in sys.stdin:
    M, K = map(int, line.split())

    durations = list(map(int, sys.stdin.readline().split()))
    playlist = list(map(int, sys.stdin.readline().split()))

    heard = set()
    total_time = 0
    answer = -1

    for song in playlist:
        total_time += durations[song - 1]
        heard.add(song)

        if len(heard) == M:
            answer = total_time
            break

    print(answer)