alcohol = gasoline = diesel = 0

while True:
    code = int(input())

    if code == 4:
        break
    elif code == 1:
        alcohol += 1
    elif code == 2:
        gasoline += 1
    elif code == 3:
        diesel += 1

print("MUITO OBRIGADO")
print(f"Alcool: {alcohol}")
print(f"Gasolina: {gasoline}")
print(f"Diesel: {diesel}")