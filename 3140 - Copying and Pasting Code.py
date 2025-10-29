body = False

while True:
    try:
        string = input()
    except EOFError:
        break

    if "<body>" in string:
        body = True
        continue

    if body and "</body>" in string:
        body = False

    if body:
        print(string)