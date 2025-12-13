number_input = input()
total_size = len(number_input)
answer = 0
n = 0

while n < total_size - 1:
    base = 10 ** n
    answer += (9 * base) * (n + 1)
    n += 1

answer += ((int(number_input) - (10 ** n)) + 1) * (n + 1)
print(answer)