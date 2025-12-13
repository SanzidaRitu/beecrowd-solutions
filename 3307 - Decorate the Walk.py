import math

pi = 3.14
n = int(input())

for i in range(n):
    a = int(input())
    r = math.sqrt(a / (4 * pi))
    text = cal_rate = None

    if r < 12:
        text = 'vermelho'
        cal_rate = 0.09
    elif 12 <= r <= 15:
        text = 'azul'
        cal_rate = 0.07
    else:
        text = 'amarelo'
        cal_rate = 0.05
    print('{text} = R$ {cost:.2f}'.format(text=text, cost=a * cal_rate))