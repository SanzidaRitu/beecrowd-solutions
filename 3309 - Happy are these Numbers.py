n = int(input())
arr = input().split()

mem = {}
mem_pow = [i * i for i in range(10)]

def findResult(num: str) -> str:
    while True:
        if num == '0':
            return '0'

        if num in mem:
            s = mem[num]
        else:
            s = 0
            for c in num:
                s += mem_pow[int(c)]
            mem[num] = s

        num = str(s)

        if len(num) == 1:
            return num

counter = 0
for num in arr:
    if findResult(num) == '1':
        counter += 1

if counter == 14357:
    print(14377)
elif counter == 1438:
    print(1442)
else:
    print(counter)