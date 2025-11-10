import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i >= len(lines):
        return

    try:
        N = int(lines[i].strip())
    except:
        return
    i += 1

    counts = {'X':0, 'H':0, 'E':0, 'A':0, 'M':0}
    read = 0

    while read < N and i < len(lines):
        line = lines[i]
        i += 1
        if line.strip() == '':
            continue

        s = line.rstrip()
        if not s:
            continue

        race = s[-1].upper()
        if race in counts:
            counts[race] += 1
        else:
            parts = line.strip().split()
            if parts:
                candidate = parts[-1].strip().upper()
                if candidate:
                    race2 = candidate[0]
                    if race2 in counts:
                        counts[race2] += 1
        read += 1

    print(f"{counts['X']} Hobbit(s)")
    print(f"{counts['H']} Humano(s)")
    print(f"{counts['E']} Elfo(s)")
    print(f"{counts['A']} Anao(oes)")
    print(f"{counts['M']} Mago(s)")

if __name__ == "__main__":
    main()