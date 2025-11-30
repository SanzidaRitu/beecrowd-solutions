class Person:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def __lt__(self, other):
        if self.time < other.time:
            return 1

    def __gt__(self, other):
        if self.time > other.time:
            return 1


n, m = map(int, input().split())
t = []

for i in range(n):
    total = 0
    x = map(int, input().split())

    for j in x:
        total += j
    t.append(Person(i + 1, total))

t.sort()
print(t[0].id)