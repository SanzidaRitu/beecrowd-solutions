def vigenere_encrypt_message(message, key):
    key_len = len(key)
    key_index = 0
    vowels = set('aeiou')
    result = []

    words = message.split(' ')

    for word in words:
        if word[0] in vowels:
            result.append(word)
            continue

        encrypted_word = []
        for ch in word:
            shift = ord(key[key_index % key_len]) - ord('a')
            new_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            encrypted_word.append(new_ch)
            key_index += 1

        result.append(''.join(encrypted_word))

    return ' '.join(result)

key = input().strip()
n = int(input())

for _ in range(n):
    line = input().strip()
    encrypted_line = vigenere_encrypt_message(line, key)
    print(encrypted_line)