Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
result = 0

if Cr > Ca:
    dc = Cr - Ca
    result += dc
if Br > Ba:
    db = Br - Ba
    result += db
if Pr > Pa:
    dp = Pr - Pa
    result += dp

print(result)