d, m = map(int, input().split('/'))

if (m == 1 and d <= 19) or (m == 12 and d >= 22):
    print("capricornio")
elif (m == 1 and d >= 20) or (m == 2 and d <= 18):
    print("aquario")
elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
    print("peixes")
elif (m == 3 and d >= 21) or (m == 4 and d <= 20):
    print("aries")
elif (m == 4 and d >= 21) or (m == 5 and d <= 20):
    print("touro")
elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
    print("gemeos")
elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
    print("cancer")
elif (m == 7 and d >= 21) or (m == 8 and d <= 22):
    print("leao")
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
    print("virgem")
elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
    print("libra")
elif (m == 10 and d >= 23) or (m == 11 and d <= 21):
    print("escorpiao")
elif (m == 11 and d >= 22) or (m == 12 and d <= 21):
    print("segitario")