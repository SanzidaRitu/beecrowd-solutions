A, B = map(int, input().split())

if 0 <= B <= 2:
    print("nova")
elif 97 <= B <= 100:
    print("cheia")
else:
    if B > A:
        print("crescente")
    else:
        print("minguante")