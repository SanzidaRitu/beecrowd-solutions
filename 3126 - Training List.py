if __name__ == "__main__":
    C, *candidates = map(int, open(0).read().split())
    print(sum(candidates))