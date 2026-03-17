import sys

def digital_root(num_str):
    if num_str == "0":
        return 0
    digit_sum = sum(int(d) for d in num_str)
    return 1 + (digit_sum - 1) % 9


for line in sys.stdin:
    n, m = line.strip().split()

    if n == "0" and m == "0":
        break

    dr_n = digital_root(n)
    dr_m = digital_root(m)

    if dr_n > dr_m:
        print(1)
    elif dr_n < dr_m:
        print(2)
    else:
        print(0)