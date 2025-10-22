dec_l = []
oct_l = []
hex_l = []

def dash():
    dash_p = ""

    for i in range(39):
        dash_p += "-"
    print(dash_p)


def line(i):
    if len(str(dec_l[i])) == 1:
        r_d_0 = "|      "

    if len(str(dec_l[i])) == 2:
        r_d_0 = "|     "

    r_d_1 = f"{dec_l[i]}    "
    r_d = r_d_0 + r_d_1

    if len(str(oct_l[i])) == 1:
        r_o_0 = "|    "

    if len(str(oct_l[i])) == 2:
        r_o_0 = "|   "

    r_o_1 = f"{oct_l[i]}    "
    r_o = r_o_0 + r_o_1
    r_h = f"|       {hex_l[i]}       |"

    output = r_d + r_o + r_h
    print(output)

for i in range(16):
    dec = i
    dec_l.append(dec)
    octal = oct(i)
    octal = octal[2:]
    oct_l.append(octal)
    hexa = hex(i)
    hexa = hexa[2:].upper()
    hex_l.append(hexa)

dash()
print("|  decimal  |  octal  |  Hexadecimal  |")
dash()
for i in range(16):
    line(i)

dash()

'|      0    |    0    |       0       |'