if __name__ == "__main__":
    n = int(input())
    num = list(input().split())
    left = right = 0
    i = 0
    j = n

    while i < j:
        if left < right:
            left += int(num[i])
            i += 1
        else:
            j -= 1
            right += int(num[j])

    if left != right:
        print(i + 1)
    else:
        print(i)