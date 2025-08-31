salary = float(input())
tax = 0.0

if salary <= 2000:
    print('Isento')
else:
    if salary <= 3000:
        tax = (salary - 2000) * 0.08
    elif salary <= 4500:
        tax = (1000 * 0.08) + (salary - 3000) * 0.18
    else:
        tax = (1000 * 0.08) + (1500 * 0.18) + (salary - 4500) * 0.28

    print(f'R$ {tax:.2f}')