t_c = int(input())

spell = {"fire":[200, 20, 30, 50],
         "water":[300, 10, 25, 40],
         "earth":[400, 25, 55, 70],
         "air":[100, 18, 38, 60]}

for i in range(t_c):

    w, h, xbl, ybl = map(int, input().split())
    power, level, cx, cy = input().split()

    level = int(level)
    cx = int(cx)
    cy = int(cy)

    for key, value in spell.items():
        if key == power:
            radius = value[level]
            break

    xbr, ybr = xbl + w, ybl

    xtl, ytl = xbl, ybl + h

    xtr, ytr = xbl + w, ybl + h

    tx, ty = cx, cy
    if cx < xbl: tx = xbl
    elif cx > xbr: tx = xbr

    if ty < ybl: ty = ybl
    elif ty > ytl: ty = ytl

    distance = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5

    '''
    #cheking is circle intersects rectangle
    if distance<=radius: print("intersects")
    else: print("does not")
    '''

    if distance <= radius:
        print(value[0])

    else:
        print("0")