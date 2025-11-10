import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    try:
        N = int(next(it))
        G = int(next(it))
    except StopIteration:
        return

    rune_values = {}
    for _ in range(N):
        try:
            rune = next(it)
            val = int(next(it))
        except StopIteration:
            break
        rune_values[rune.upper()[0]] = val

    try:
        X = int(next(it))
    except StopIteration:
        X = 0

    remaining = ''.join(list(it))
    letters = []
    for ch in remaining:
        if ch.isalpha():
            letters.append(ch.upper())
            if len(letters) == X:
                break

    total = sum(rune_values.get(ch, 0) for ch in letters)
    print(total)
    print("You shall pass!" if total >= G else "My precioooous")

if __name__ == "__main__":
    solve()