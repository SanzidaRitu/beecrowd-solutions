salary = float(input())

if salary <= 400.00:
    percent = 15
elif salary <= 800.00:
    percent = 12
elif salary <= 1200.00:
    percent = 10
elif salary <= 2000.00:
    percent = 7
else:
    percent = 4

increase = salary * percent / 100
newsal = salary + increase

print(f'Novo salario: {newsal:.2f}')
print(f'Reajuste ganho: {increase:.2f}')
print(f'Em percentual: {percent} %')