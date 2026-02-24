S = input().strip()

grades = []
i = 0
n = len(S)

while i < n:
    if S[i] == '1' and i + 1 < n and S[i + 1] == '0':
        grades.append(10)
        i += 2
    else:
        grades.append(int(S[i]))
        i += 1

average = sum(grades) / len(grades)

print(f"{average:.2f}")