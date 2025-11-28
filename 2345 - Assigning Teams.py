if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    answer = abs((a + d) - (b + c))
    print(answer)