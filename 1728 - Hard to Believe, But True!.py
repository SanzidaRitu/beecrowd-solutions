import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    left, c = line.split('=')
    a, b = left.split('+')

    ra = int(a[::-1])
    rb = int(b[::-1])
    rc = int(c[::-1])

    if ra + rb == rc:
        print("True")
    else:
        print("False")