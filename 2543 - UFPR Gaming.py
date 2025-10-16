while True:
    try:
        N, I = map(int,input().split())

        list_uni_id = []
        list_game_name = []

        for num in range(N):
            i , j = map(int, input().split())
            list_uni_id.append(i)
            list_game_name.append(j)

        result = 0

        for item in range(N):
            if list_uni_id[item - 1] == I and list_game_name[item - 1] == 0:
                result += 1

        print(result)

    except EOFError:
        break