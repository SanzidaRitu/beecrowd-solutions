A1 = int(input())
A2 = int(input())
A3 = int(input())

time = []

t1 = A2 * 2 + A3 * 4
t2 = A1 * 2 + A3 * 2
t3 = A1 * 4 + A2 * 2

time.append(t1)
time.append(t2)
time.append(t3)

time.sort()
print(time[0])