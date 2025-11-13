import sys

def is_bad_key(K, L):
    for p in range(2, L):
        if K % p == 0:
            return f"BAD {p}"
    return "GOOD"

def main():
    while True:
        line = input().strip()
        if line == "":
            continue

        K_str, L_str = line.split()
        K = int(K_str)
        L = int(L_str)

        if K == 0 and L == 0:
            break

        print(is_bad_key(K, L))

if __name__ == "__main__":
    main()