l, n = map(int, input().split())

irregular = {}

for _ in range(l):
    s, p = input().split()
    irregular[s] = p

vowels = "aeiou"

for _ in range(n):
    word = input().strip()

    if word in irregular:
        print(irregular[word])

    elif word.endswith('y') and word[-2] not in vowels:
        print(word[:-1] + "ies")

    elif word.endswith(('o', 's', 'x', 'ch', 'sh')):
        print(word + "es")

    else:
        print(word + "s")