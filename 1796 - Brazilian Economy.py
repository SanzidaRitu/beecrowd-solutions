Q = int(input().strip())

opinions = list(map(int, input().split()))

count_zero = opinions.count(0)
count_one = opinions.count(1)

if count_zero > count_one:
    print("Y")
else:
    print("N")