def double_string(S):
    X = int(S)
    X = str(X)
    if len(X) == 1:
        Y = "0" + X

    else:
        Y = X

    return Y


while True:
    try:
        N = float(input())

        Sec = N * 240
        Min = Sec // 60
        Hr = (Min // 60)


        '''
        print(f"Degree = {N}")
        print(f"Sec = {Sec}")
        print(f"Min = {Min}")
        print(f"Hr = {Hr}")
        '''

        Sec = Sec - (Min * 60)
        Min = Min - (Hr * 60)

        if 0 <= N < 90 or N == 360:
            Hr = Hr + 6
            print("Bom Dia!!")

        elif 90 <= N < 180:
            Hr = Hr + 6
            print("Boa Tarde!!")

        elif 180 <= N < 270:
            Hr = Hr + 6
            print("Boa Noite!!")

        elif 270 <= N < 360:
            Hr = Hr - 18
            print("De Madrugada!!")

        Sec_str = double_string(Sec)
        Min_str = double_string(Min)
        Hr_str = double_string(Hr)

        print(f"{Hr_str}:{Min_str}:{Sec_str}")

    except EOFError:
        break