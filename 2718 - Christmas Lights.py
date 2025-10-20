def consecutive(X):
    bin_str = list(X)
    highest_count_list = []
    count = 0

    for i in range(len(bin_str)):
        X = bin_str[i]

        if X == "1":
            count += 1

        elif X == "0":
            highest_count_list.append(count)
            count = 0

        if i == len(bin_str) - 1:
            highest_count_list.append(count)

    highest_count_list.sort(reverse = True)
    highest_count = highest_count_list[0]

    return highest_count

N = int(input())

for i in range(N):
    dec_val = int(input())
    bin_val = bin(dec_val)[2:]

    answer = consecutive(bin_val)
    print(answer)