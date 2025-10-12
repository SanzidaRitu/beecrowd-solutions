S = input()
extra = []

for i in S:
    if i == "1":
        extra.append(i)

length = len(extra)

if (length % 2) != 0 and length > 0:
    S += "1"

else:
    S += "0"

print(S)