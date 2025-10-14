while True:
    try:
        msg = input()
        count = int(input())
        count_list = list(map(int, input().split()))

        output = []

        for num in count_list:
            output.append(msg[num - 1])

        result = "".join(output)
        print(result)

    except EOFError:
        break