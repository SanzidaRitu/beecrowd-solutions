def has_number(s):
    for char in s:
        if char.isdigit():
            return True
    return False

n = int(input())

while n:
    n -= 1
    plate = input().split('-')

    if (len(plate) == 2) and (len(plate[0]) == 3) and (len(plate[1]) == 4) and (
            plate[0] == plate[0].upper() and (has_number(plate[0]) == False)):
        try:
            check = int(plate[1])
            r = int(plate[1][3])

            if r > 8 or r == 0:
                print('FRIDAY')

            elif r > 6:
                print('THURSDAY')

            elif r > 4:
                print('WEDNESDAY')

            elif r > 2:
                print('TUESDAY')

            elif r > 0:
                print('MONDAY')

            else:
                print('FAILURE')

        except:
            print('FAILURE')
    else:
        print('FAILURE')