import sys

def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

while True:
    try:
        N = int(input())
        if N == 0:
            break

        u_score = 0
        r_score = 0
        i_score = 0

        for _ in range(N):
            U, R, I = map(int, input().split())

            max_value = max(U, R, I)

            if is_power_of_two(U):
                u_score += 1
                if U == max_value:
                    u_score += 1

            if is_power_of_two(R):
                r_score += 1
                if R == max_value:
                    r_score += 1

            if is_power_of_two(I):
                i_score += 1
                if I == max_value:
                    i_score += 1

        if u_score > r_score and u_score > i_score:
            print("Uilton")
        elif r_score > u_score and r_score > i_score:
            print("Rita")
        elif i_score > u_score and i_score > r_score:
            print("Ingred")
        else:
            print("URI")

    except EOFError:
        break