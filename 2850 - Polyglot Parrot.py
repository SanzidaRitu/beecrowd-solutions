import sys

m = {
    "esquerda": "ingles",
    "direita":  "frances",
    "nenhuma":  "portugues",
    "as duas":  "caiu"
}

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue

    out = m.get(s)
    if out is not None:
        print(out)
    else:
        pass