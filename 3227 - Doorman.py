def main():
    K = int(input().strip())
    queue = list(input().strip())

    men = women = 0
    entered = 0

    while queue:
        def can_enter(ch):
            if ch == 'M':
                return abs((men + 1) - women) <= K
            else:
                return abs(men - (women + 1)) <= K

        if can_enter(queue[0]):
            ch = queue.pop(0)
        elif len(queue) > 1 and can_enter(queue[1]):
            ch = queue.pop(1)
        else:
            break

        if ch == 'M':
            men += 1
        else:
            women += 1

        entered += 1

    print(entered)

if __name__ == "__main__":
    main()