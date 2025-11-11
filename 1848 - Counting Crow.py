import sys

current_sum = 0
screams_count = 0

for line in sys.stdin:
    line = line.strip()

    if line == "caw caw":
        print(current_sum)

        current_sum = 0
        screams_count += 1

        if screams_count == 3:
            break
    else:
        binary_str = line.replace('*', '1').replace('-', '0')
        value = int(binary_str, 2)
        current_sum += value