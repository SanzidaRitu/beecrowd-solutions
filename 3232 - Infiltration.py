import sys
from itertools import combinations
from functools import lru_cache

KNOWN = [
    "be","our","rum","will",
    "dead","hook","ship","blood",
    "sable","avenge","parrot","captain"
]

def pattern_signature(s):
    m = {}
    next_id = 0
    sig = []
    for ch in s:
        if ch not in m:
            m[ch] = next_id
            next_id += 1
        sig.append(m[ch])
    return tuple(sig)

def bitcount(x):
    return bin(x).count("1")

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    text = data[0].strip()
    words = text.split()

    cipher_set = set(ch for ch in text if ch != ' ')
    K = len(cipher_set)

    known_masks = []
    known_sigs = []
    for w in KNOWN:
        mask = 0
        for ch in w:
            mask |= 1 << (ord(ch) - ord('a'))
        known_masks.append(mask)
        known_sigs.append(pattern_signature(w))

    cipher_sigs = [pattern_signature(w) for w in words]

    n_known = len(KNOWN)
    n_words = len(words)

    candidates_for_known = []
    for ki, kw in enumerate(KNOWN):
        cand = []
        lkw = len(kw)
        sig_kw = known_sigs[ki]
        for i, cw in enumerate(words):
            if len(cw) != lkw:
                continue
            if cipher_sigs[i] != sig_kw:
                continue
            cand.append(i)
        candidates_for_known.append(cand)

    all_plaintexts = set()

    cipher_letters_mask = 0
    for ch in cipher_set:
        cipher_letters_mask |= 1 << (ord(ch) - ord('a'))

    for mask in range(1, 1 << n_known):
        union_mask = 0
        subset_indices = []
        for k in range(n_known):
            if (mask >> k) & 1:
                union_mask |= known_masks[k]
                subset_indices.append(k)
        if bitcount(union_mask) != K:
            continue

        cand_lists = []
        possible = True
        for k in subset_indices:
            cand = candidates_for_known[k]
            if not cand:
                possible = False
                break
            cand_lists.append((k, cand))
        if not possible:
            continue

        cand_lists.sort(key=lambda x: len(x[1]))

        used_pos = [False] * n_words

        map_c2p = [-1] * 26
        map_p2c = [-1] * 26

        def assign_word(idx):
            if idx == len(cand_lists):
                mapped_mask = 0
                for c in range(26):
                    if map_c2p[c] != -1:
                        mapped_mask |= 1 << c

                if mapped_mask != cipher_letters_mask:
                    return

                res_chars = []
                for ch in text:
                    if ch == ' ':
                        res_chars.append(' ')
                    else:
                        p = map_c2p[ord(ch) - ord('a')]
                        if p == -1:
                            return
                        res_chars.append(chr(p + ord('a')))
                all_plaintexts.add(''.join(res_chars))
                return

            k, cand = cand_lists[idx]
            plain_word = KNOWN[k]

            for pos in cand:
                if used_pos[pos]:
                    continue

                cw = words[pos]
                changed = []
                changed_rev = []
                ok = True
                for cch, pch in zip(cw, plain_word):
                    ci = ord(cch) - ord('a')
                    pi = ord(pch) - ord('a')
                    if map_c2p[ci] == -1 and map_p2c[pi] == -1:
                        map_c2p[ci] = pi
                        map_p2c[pi] = ci
                        changed.append((ci, -1))
                        changed_rev.append((pi, -1))
                    elif map_c2p[ci] == pi and map_p2c[pi] == ci:
                        pass
                    else:
                        ok = False
                        break
                if ok:
                    used_pos[pos] = True
                    assign_word(idx + 1)
                    used_pos[pos] = False

                for ci, prev in changed:
                    if prev == -1:
                        map_c2p[ci] = -1
                for pi, prev in changed_rev:
                    if prev == -1:
                        map_p2c[pi] = -1

        assign_word(0)

        if len(all_plaintexts) > 1:
            break

    if len(all_plaintexts) == 1:
        print(next(iter(all_plaintexts)))
    else:
        print("Impossible")

if __name__ == "__main__":
    solve()