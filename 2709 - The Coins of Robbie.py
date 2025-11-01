def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        m = int(input())

        coins = [int(input()) for _ in range(m)]

        jump = int(input())

        coins.reverse()

        total = sum(coins[i] for i in range(0, m, jump))

        if is_prime(total):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")

        else:
            print("Bad boy! I’ll hit you.")

    except EOFError:
        break