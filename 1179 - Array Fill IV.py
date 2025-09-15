par = [0] * 5
impar = [0] * 5
par_count = 0
impar_count = 0

for _ in range(15):
    num = int(input())

    if num % 2 == 0:
        par[par_count] = num
        par_count += 1
        if par_count == 5:
            for i in range(5):
                print(f"par[{i}] = {par[i]}")
            par_count = 0
    else:
        impar[impar_count] = num
        impar_count += 1
        if impar_count == 5:
            for i in range(5):
                print(f"impar[{i}] = {impar[i]}")
            impar_count = 0

for i in range(impar_count):
    print(f"impar[{i}] = {impar[i]}")
for i in range(par_count):
    print(f"par[{i}] = {par[i]}")