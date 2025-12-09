import re

if __name__ == "__main__":
    input_ = input().replace(" ", "")
    input_ = input_.replace("7", "0")
    a, b = re.split('[+x]', input_)
    answer = 0

    if input_.find('+') != -1:
        answer = int(a) + int(b)
        answer = str(answer).replace('7', '0')
    else:
        answer = int(a) * int(b)
        answer = str(answer).replace('7', '0')

    print(int(answer))