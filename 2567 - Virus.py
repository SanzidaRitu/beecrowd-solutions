from sys import stdin

while True:
    line = stdin.readline()
    if line == '':
        break
    elif not line[0].isdigit():
        continue

    n = int(line)
    numberList = list(map(int, stdin.readline().split()))
    numberList.sort()
    mid = int(n / 2)
    e = n - 1
    sum = 0

    for i in range(0, mid):
        sum += numberList[e - i] - numberList[i]

    print(sum)