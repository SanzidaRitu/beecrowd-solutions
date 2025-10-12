A, B, C = map(int, input().split())
result = ""

if (A - B) == 0 or (B - C) == 0 or (C - A) == 0:
    result = "S"

else:
    result = "N"

    binary_list = []

    for decimal_num in range(8):
        binary_num = bin(decimal_num)[2:].zfill(3)
        converted_num = [-1 if bit == '1' else 1 for bit in binary_num]
        binary_list.append(converted_num)

    for i in range(8):
        a = binary_list[i][0]
        b = binary_list[i][1]
        c = binary_list[i][2]

        A1 = A * a
        B1 = B * b
        C1 = C * c

        output = A1 + B1 + C1

        if output == 0:
            result = "S"
            break

        else:
            result = "N"

print(result)