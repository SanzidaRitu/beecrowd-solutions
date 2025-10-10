C = int(input())

for i in range(C):
    letter = input()
    length = len(letter)
    time = length / 100

    print(f'{time:.2f}')