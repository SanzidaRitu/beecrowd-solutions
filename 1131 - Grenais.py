grenais = inter = gremio = draws = 0

while True:
    i, g = map(int, input().split())
    grenais += 1
    inter += i > g
    gremio += g > i
    draws += i == g

    print("Novo grenal (1-sim 2-nao)")
    if int(input()) == 2:
        break

print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{draws}")
print("Inter venceu mais" if inter > gremio else "Gremio venceu mais" if gremio > inter else "Nao houve vencedor")