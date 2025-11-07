n = int(input())

fib = [1, 2]
while fib[-1] < 100000:
    fib.append(fib[-1] + fib[-2])

fib_set = set(fib)

count = 0
num = 1

while True:
    if num not in fib_set:
        count += 1
        if count == n:
            print(num)
            break
    num += 1